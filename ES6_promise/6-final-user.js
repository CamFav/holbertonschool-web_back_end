import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

const handleProfileSignup = async () => {
  let photo;
  let user;

  try {
    [photo, user] = await Promise.all([uploadPhoto(), signUpUser()]);
  } catch (err) {
    photo = null;
    user = null;
  }

  return {
    photo,
    user,
  };
};

export default handleProfileSignup;
