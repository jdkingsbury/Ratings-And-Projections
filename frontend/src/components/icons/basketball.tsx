import React from "react";

const BasketballIcon = (props: React.SVGProps<SVGSVGElement>) => (
  <svg
    xmlns="http://www.w3.org/2000/svg"
    viewBox="0 0 24 24"
    width={24}
    height={24}
    color={"#000000"}
    fill={"none"}
    {...props}
  >
    <path
      d="M22 12C22 17.5228 17.5228 22 12 22C6.47715 22 2 17.5228 2 12C2 6.47715 6.47715 2 12 2C17.5228 2 22 6.47715 22 12Z"
      stroke="currentColor"
      strokeWidth="1.5"
    />
    <path
      d="M2 12.9506C8.14512 13.5607 13.5577 8.11477 12.9506 2"
      stroke="currentColor"
      strokeWidth="1.5"
    />
    <path
      d="M11.0507 22.0012C10.4406 15.856 15.8866 10.4434 22.0013 11.0505"
      stroke="currentColor"
      strokeWidth="1.5"
    />
    <path
      d="M17 20C17 12.8203 11.1797 7 4 7"
      stroke="currentColor"
      strokeWidth="1.5"
      strokeLinecap="round"
    />
  </svg>
);

export default BasketballIcon;
