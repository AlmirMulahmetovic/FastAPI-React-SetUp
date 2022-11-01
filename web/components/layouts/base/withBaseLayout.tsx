import Footer from "@/components/footer";
import Navbar from "@/components/navbar";
import { Container, Box } from "@mui/system";
import React from "react";

const withBaseLayout = (WrappedComponent: any) => {
  return (props: object) => {
    return (
      <Box sx={{ minHeight: "100vh", height: "100vh" }}>
        <Navbar />
        <Container>
          <WrappedComponent {...props} />;
        </Container>
        <Footer />
      </Box>
    );
  };
};

export default withBaseLayout;
