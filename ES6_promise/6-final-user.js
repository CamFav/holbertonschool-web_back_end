import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
  const userPromise = signUpUser(firstName, lastName);
  const photoPromise = uploadPhoto(fileName);

  return Promise.all([userPromise, photoPromise])
    .then(([userResult, photoResult]) => {
      return [
        { status: 'fulfilled', value: userResult },
        { status: 'fulfilled', value: photoResult }
      ];
    })
    .catch((error) => {
      return [{ status: 'rejected', value: error }];
    });
}
