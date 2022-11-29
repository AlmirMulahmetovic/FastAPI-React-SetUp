/** @type {import('next').NextConfig} */
const nextConfig = {
    reactStrictMode: true,
    swcMinify: true,
    publicRuntimeConfig: {
        API_URL: process.env.API_URL || 'http://localhost:8000'
    },
    async redirects() {
        return [
            {
                source: '/login',
                has: [
                    {
                        type: 'cookie',
                        key: 'access_token',
                    },
                ],
                permanent: false,
                destination: '/',
            },
        ]
    },
}

module.exports = nextConfig
