import React from "react";

import Typography from "@mui/material/Typography";
import Link from "next/link";

import styles from "@/styles/navbar/NavTitle.module.scss";

interface OwnProps {
  title: string;
}

export const NavTitle = ({ title }: OwnProps) => {
  return (
    <Typography variant="h6" color="inherit" noWrap sx={{ flexGrow: 1 }}>
      <Link href="/">
        <a className={styles.navTitle}>{title}</a>
      </Link>
    </Typography>
  );
};
