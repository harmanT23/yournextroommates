import statusCodes from 'http-status-codes';
import axiosInstance from "../api/axiosInstance";
import {
  FETCH_LISTING_LIST,
  FETCH_LISTING,
} from './types';


export const fetchListingList = () => async (dispatch) => {
  /* Fetches a list of listings
   */
  const res = await axiosInstance.get('/listings/')
  if (!res || res.status !== statusCodes.OK) {
    return false;
  } else {
    dispatch({type: FETCH_LISTING_LIST, payload: res.data})
    return true;
  }
}

export const fetchListing = (listingSlug) => async (dispatch) => {
  /* Fetches listing by ID
   */
  const res = await axiosInstance.get('/listings/' + String(listingSlug) + '/')
  .catch(() => {
    return false;
  });

  if (!res || res.status !== statusCodes.OK) {
    return false;
  } else {
    dispatch({type: FETCH_LISTING, payload: res.data})
    return true;
  }
}
