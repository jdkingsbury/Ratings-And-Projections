import { env } from "next-runtime-env";

export const BACKEND_API_BASE_URL = env("NEXT_PUBLIC_BACKEND_API_BASE_URL");
export const BACKEND_WS_BASE_URL = env("NEXT_PUBLIC_BACKEND_WS_BASE_URL");
