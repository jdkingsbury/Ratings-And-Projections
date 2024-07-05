export const omitKeys = <T>(obj: T, keys: (keyof T)[]): Partial<T> => {
  const result: Partial<T> = { ...obj };
  keys.forEach((key) => {
    delete result[key];
  });
  return result;
};
