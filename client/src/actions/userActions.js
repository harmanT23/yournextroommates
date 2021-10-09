import statusCodes from 'http-status-codes';
import axiosInstance from "../api/axiosInstance";
import {
  REGISTER,
  LOGIN,
  LOGOUT,
  FETCH_AUTH_USER,
  FETCH_USER,
} from './types';


export const registerUser = (userData) => async (dispatch) => {
  /* Register new user where userData consists of the following
   * - Email 
   * - Password
   * - First Name
   * - Last Name
   * - Date of Birth: yyyy-mm-dd
   * - City 
   * - Province
   * - Profile Image
   */
  const res = await axiosInstance.post('/users/', userData)

  if (!res || res.status !== statusCodes.CREATED) {
    return false;
  } else {
    dispatch({type: REGISTER, payload: null});
    return true;
  }
}

export const loginUser = (userData) => async (dispatch) => {
  /* Login and obtain refresh/access token where userData
   * consists of email and password
   */

  const res = await axiosInstance.post('/token/', {
      email: userData.email,
      password: userData.password,
    });

    if (!res || res.status !== statusCodes.OK) {
      return false;
    } else {
      dispatch({type: LOGIN, payload: res.data});
      return res.data;
    }
}

export const logoutUser = () => async (dispatch) => {
  /* Login and obtain refresh/access token where userData
   * consists of username and password
   */
  await axiosInstance.post('/token/blacklist/',{
    refresh_token: localStorage.getItem('refresh_token'),
  });
  dispatch({type: LOGOUT, payload: null})
}


export const fetchAuthUser = () => async (dispatch) => {
  /* Fetches the currently authenticated user
   */
  const res = await axiosInstance.get('/users/me/').catch(() => {
    return false;
  });

  if (!res || res.status !== statusCodes.OK) {
    return false;
  } else {
    dispatch({type: FETCH_AUTH_USER, payload: res.data})
    return true;
  }
}


export const fetchUser = (userID) => async (dispatch) => {
  /* Fetches user by ID
   */
  const res = await axiosInstance.get('/users/' + String(userID) + '/')
  .catch(() => {
    return false;
  });

  if (!res || res.status !== statusCodes.OK) {
    return false;
  } else {
    dispatch({type: FETCH_USER, payload: res.data})
    return true;
  }
}
