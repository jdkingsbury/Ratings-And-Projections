export const omitKeys = <T>(obj: T, keys: (keyof T)[]): Partial<T> => {
  const result = { ...obj };
  keys.forEach((key) => {
    delete result[key];
  });
  return result;
};
