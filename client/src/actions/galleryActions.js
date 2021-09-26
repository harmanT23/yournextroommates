import statusCodes from 'http-status-codes';
import axiosInstance from "../api/axiosInstance";
import {
  UPLOAD_GALLERY,
  FETCH_GALLERY,
} from './types';


export const uploadGallery = (galleryData) => async (dispatch) => {
  /* Uploads a new gallery where galleryData is a set of images
   * and contains a flag if the gallery is for a listing or user
   */
  const res = await axiosInstance.post('/galleries/', galleryData)

  if (!res || res.status !== statusCodes.CREATED) {
    return false;
  } else {
    dispatch({type: UPLOAD_GALLERY, payload: null});
    return true;
  }
}


export const fetchGallery = (galleryID) => async (dispatch) => {
  /* Fetches user by ID
   */
  const res = await axiosInstance.get('/galleries/' + String(galleryID) + '/')
  .catch(() => {
    return false;
  });

  if (!res || res.status !== statusCodes.OK) {
    return false;
  } else {
    dispatch({type: FETCH_GALLERY, payload: res.data})
    return true;
  }
}
