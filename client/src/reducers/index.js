import { combineReducers } from 'redux';
import userReducer from './userReducers';
import listingReducer from './listingReducers';
import galleryReducer from './galleryReducers';
import imageReducer from './imageReducers';

export default combineReducers({
  userData: userReducer,
  listingData: listingReducer,
  galleryData: galleryReducer,
  imageData: imageReducer
})
