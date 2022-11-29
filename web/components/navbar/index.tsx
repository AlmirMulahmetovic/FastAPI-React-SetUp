import React, { useEffect, useState } from "react";
import AppBar from "@mui/material/AppBar";
import Button from "@mui/material/Button";
import CssBaseline from "@mui/material/CssBaseline";
import Toolbar from "@mui/material/Toolbar";
import GlobalStyles from "@mui/material/GlobalStyles";
import { NavLink } from "./NavLink";
import { NavTitle } from "./NavTitle";
import { getIsLoggedIn } from "@/util/localStorage"
import { logout } from "@/app/features/auth/logout"
import { useRouter } from "next/router";

function Navbar() {
  const [isLoggedIn, setIsLoggedIn] = useState<boolean | null>(null)
  const router = useRouter()


  useEffect(
    () => {
      setIsLoggedIn(getIsLoggedIn())
    }, []
  )

  const onLogoutClick = async (event: any) => {
    event.preventDefault()
    const logoutResponse = await logout()
    if(logoutResponse.status === 200){
      setIsLoggedIn(false)
      router.push("/login")
    }
  }

  return (
    <React.Fragment>
      <GlobalStyles
        styles={{ ul: { margin: 0, padding: 0, listStyle: "none" } }}
      />
      <CssBaseline />
      <AppBar
        position="static"
        color="default"
        elevation={0}
        sx={{ borderBottom: (theme) => `1px solid ${theme.palette.divider}` }}
      >
        <Toolbar sx={{ flexWrap: "wrap" }}>
          <NavTitle title="Best Bet" />
          <nav>
            <NavLink href="/pokemon" label="Features" />
            <NavLink href="/pokemon" label="Pokemon" />
            <NavLink href="/pokemon" label="Support" />
          </nav>
          {
            router.pathname !== "/login" && 
            (
              !isLoggedIn ?
              <Button href="/login" variant="outlined" sx={{ my: 1, mx: 1.5 }}>
                Login
              </Button> : 
              <Button onClick={onLogoutClick} variant="outlined" sx={{ my: 1, mx: 1.5 }}>
                Logout
              </Button>
            )
          }
        </Toolbar>
      </AppBar>
    </React.Fragment>
  );
}

export default Navbar;
