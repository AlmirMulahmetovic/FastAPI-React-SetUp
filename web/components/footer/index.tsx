import React from "react";
import Copyright from "./copyright";

import Box from "@mui/system/Box";

function Footer() {
  return (
    <Box
      sx={{
        position: "fixed",
        bottom: 0,
        justifyContent: "center",
        width: "100%",
        marginBottom: "1rem",
      }}
    >
      <Copyright />
    </Box>
  );
}

export default Footer;
