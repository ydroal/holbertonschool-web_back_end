import { uploadPhoto, createUser } from './utils';

export default async function asyncUploadUser() {
  const res = {
    photo: null,
    user: null,
  };

  const results = await Promise.allSettled([uploadPhoto(), createUser()]);
  results.forEach((result, index) => {
    if (result.status === 'rejected') {
      return res;
    }
    if (index === 0) {
      res.photo = result.value;
    } else {
      res.user = result.value;
    }
  });
  return res;
}
