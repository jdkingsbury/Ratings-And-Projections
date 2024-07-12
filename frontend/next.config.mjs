/** @type {import('next').NextConfig} */
const nextConfig = {
  output: "standalone",
  images: {
    remotePatterns: [
      {
        protocol: "https",
        hostname: "ak-static.cms.nba.com",
        port: "",
      },
    ],
  },
};

export default nextConfig;
