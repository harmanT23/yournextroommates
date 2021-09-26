import axios from 'axios'
import statusCodes from 'http-status-codes';

const baseURL = 'http://127.0.0.1:8000/api'

const axiosInstance = axios.create({
  baseURL: baseURL,
  timeout: 5000,
  headers: {
    Authorization: (localStorage.getItem('access_token') !== 'undefined' &&
                    localStorage.getItem('access_token') !== null)
                      ? 'JWT ' + localStorage.getItem('access_token')
                      : null,
    'Content-Type': 'application/json',
    accept: 'application/json',
  },
});

axiosInstance.interceptors.response.use(
  (response) => {
    return response;
  },

  async function (error) {
    const originalRequest = error.config;
    // Handle server failure
    if (typeof error.response === 'undefined') {
      alert(
        'Timeout. A server or network error occurred.'
      );
      window.location.href = '/';
      return Promise.reject(error);
    }

    // Prevent repeating token refresh with failure (i.e. catch 2nd
    // attempt at trying to acquire refresh token)
    if ( 
      error.response.status === statusCodes.UNAUTHORIZED &&
      originalRequest.url === (baseURL + '/token/refresh/')
    ) {
        localStorage.removeItem('access_token');
        localStorage.removeItem('refresh_token');
        window.location.href = '/login/';
        return Promise.reject(error);
    }

    // Handle expired access token and get new one
    if (
      error.response.data.code === 'token_not_valid' &&
      error.response.status === statusCodes.UNAUTHORIZED &&
      error.response.statusText === 'Unauthorized'
    ) {
        const refreshToken = localStorage.getItem('refresh_token');
        if (refreshToken && refreshToken !== 'undefined') {
          const tokenParts = JSON.parse(atob(refreshToken.split('.')[1]));
          const now = Math.ceil(Date.now() / 1000);
          
          if (tokenParts.exp > now) { // Token is expired get a new one
            return axiosInstance.post(
              '/token/refresh/', 
              { refresh: refreshToken }
            ).then((response) => {
                localStorage.setItem('access_token', response.data.access);
                localStorage.setItem('refresh_token', response.data.refresh);

                axiosInstance.defaults.headers['Authorization'] =
                  'JWT ' + response.data.access;

                originalRequest.headers['Authorization'] =
                  'JWT ' + response.data.access;

                return axiosInstance(originalRequest);
              }).catch((err) => {
                console.log(err);
                localStorage.removeItem('access_token');
                localStorage.removeItem('refresh_token');
              });
          } else {
            console.log('Refresh token is expired', tokenParts.exp, now);
            localStorage.removeItem('access_token');
            localStorage.removeItem('refresh_token');
            window.location.href = '/login/';
          }
        } else {
          console.log('Refresh token not available.');
          localStorage.removeItem('access_token');
          localStorage.removeItem('refresh_token');
          window.location.href = '/login/';
        }
    }
    return Promise.reject(error);
  }
);

export default axiosInstance