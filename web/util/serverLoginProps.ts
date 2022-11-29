import type { GetServerSidePropsResult, GetServerSidePropsContext } from "next";

export default async ({req}: GetServerSidePropsContext): Promise<GetServerSidePropsResult<any>> => {
    if(req.cookies.access_token === undefined){
      return {
        redirect: {
          destination: '/login',
          permanent: false,
        },
      }
    }
    return {
      props: {}, // will be passed to the page component as props
    }
  }
