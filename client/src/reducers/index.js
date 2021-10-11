import { combineReducers } from 'redux';
import userReducer from './userReducers';
import listingReducer from './listingReducers';
import galleryReducer from './galleryReducers';
import imageReducer from './imageReducers';
import sUserReducer from './sUserReducers';

export default combineReducers({
  userData: userReducer,
  sUserData: sUserReducer,
  listingData: listingReducer,
  galleryData: galleryReducer,
  imageData: imageReducer
})
