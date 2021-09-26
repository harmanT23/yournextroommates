import statusCodes from 'http-status-codes';
import axiosInstance from "../api/axiosInstance";
import { FETCH_IMAGE } from './types';


export const fetchImage = (imageData) => async (dispatch) => {
  /* Fetches user by ID
   */
  const res = await axiosInstance.get(
    '/galleries/' + String(imageData.galleryID) + '/' + String(imageData.imageID) + '/'
  ).catch(() => {
    return false;
  });

  if (!res || res.status !== statusCodes.OK) {
    return false;
  } else {
    dispatch({type: FETCH_IMAGE, payload: res.data})
    return true;
  }
}
