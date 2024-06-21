import { Link } from "@remix-run/react";
import { NavLink } from "@remix-run/react";
import { useState } from "react";
import { Button, buttonVariants } from "~/components/ui/button";
import {
  NavigationMenu,
  NavigationMenuContent,
  NavigationMenuIndicator,
  NavigationMenuItem,
  NavigationMenuLink,
  NavigationMenuList,
  NavigationMenuTrigger,
  NavigationMenuViewport,
  navigationMenuTriggerStyle,
} from "~/components/ui/navigation-menu";

// TODO: Work on mobile navigation

export default function Navbar() {
  const [isMobileMenuOpen, setMobileMenuOpen] = useState(false);

  const toggleMobileMenu = () => {
    setMobileMenuOpen(!isMobileMenuOpen);
  };

  return (
    <div className="flex w-full bg-white h-16 sticky top-0 border-b border-gray-100">
      <div className="container mx-auto px-4 h-full flex items-center justify-between">
        <div className="md:hidden flex items-center">
          <Button onClick={toggleMobileMenu} variant="ghost">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 24 24"
              strokeWidth={1.5}
              stroke="currentColor"
              className="size-6"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                d="M3.75 6.75h16.5M3.75 12h16.5m-16.5 5.25h16.5"
              />
            </svg>
          </Button>
        </div>
        <div className="hidden md:flex md:flex-row flex-col items-center justify-start md:space-x-1 space-x-6">
          <NavLink to="/" className={buttonVariants({ variant: "ghost" })}>
            Home
          </NavLink>
          <NavigationMenu>
            <NavigationMenuList>
              <NavigationMenuItem>
                <NavigationMenuTrigger>NBA</NavigationMenuTrigger>
                <NavigationMenuContent>
                  <Link to="/players">
                    <NavigationMenuLink
                      className={navigationMenuTriggerStyle()}
                    >
                      Players
                    </NavigationMenuLink>
                  </Link>
                </NavigationMenuContent>
              </NavigationMenuItem>
            </NavigationMenuList>
          </NavigationMenu>
        </div>
      </div>
    </div>
  );
}
