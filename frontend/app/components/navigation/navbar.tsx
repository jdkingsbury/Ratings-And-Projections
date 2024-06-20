import { Link } from "@remix-run/react";
import { NavLink } from "@remix-run/react";
import { buttonVariants } from "~/components/ui/button";
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
} from "~/components/ui/navigation-menu"

export default function Navbar() {
  return (
    <div className="flex w-full bg-white h-16 sticky top-0 border-b border-gray-100">
      <div className="container mx-auto px-4 h-full flex items-center justify-between">
        <ul className="hidden md:flex space-x-6">
          <li>
            <Link to="/" className={buttonVariants({ variant: "ghost" })}>Home</Link>
          </li>
          <li>
            <NavigationMenu>
              <NavigationMenuList>
                <NavigationMenuItem>
                  <NavigationMenuTrigger>NBA</NavigationMenuTrigger>
                  <NavigationMenuContent>
                    <Link to="/players">
                      <NavigationMenuLink className={navigationMenuTriggerStyle()}>
                        Players
                      </NavigationMenuLink>
                    </Link>
                  </NavigationMenuContent>
                </NavigationMenuItem>
              </NavigationMenuList>
            </NavigationMenu>
          </li>
        </ul>
      </div>
    </div>
  );
}
