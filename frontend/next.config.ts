import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  /* config options here */
  images:{
    remotePatterns: [new URL("https://lalucha.com.pe/wp-content/uploads/**")]
  }
};

export default nextConfig;
