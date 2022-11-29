import React from "react";
import Link from "next/link";

import styles from "@/styles/navbar/NavLink.module.scss";

interface OwnProps {
  href: string;
  label: string;
}

export const NavLink = ({ href, label }: OwnProps) => {
  return (
    <Link href={href}>
      <a className={styles.navLink}>{label}</a>
    </Link>
  );
};
