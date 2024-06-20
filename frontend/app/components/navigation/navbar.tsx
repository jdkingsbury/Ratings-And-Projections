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


// export default function Navbar() {
//   return (
//     <div className="flex w-full h-16 bg-black sticky top-0">
//       <div className="container mx-auto px-4 h-full">
//         <div className="flex justify-between items-center h-full">
//           <nav className="flex w-full gap-4">
//             <ul className="hidden md:flex gap-x-6 text-white">
//               <li>
//                 <NavLink
//                   to="/"
//                   className={({ isActive }) => (isActive ? "font-bold" : "")}
//                 >
//                   Home
//                 </NavLink>
//               </li>
//               <li>
//                 <NavLink
//                   to="/players"
//                   className={({ isActive }) => (isActive ? "font-bold" : "")}
//                 >
//                   Players
//                 </NavLink>
//               </li>
//             </ul>
//           </nav>
//         </div>
//
//       </div>
//     </div>
//   );
// }
//
export default function Navbar() {
  return (
    <div className="flex w-full h-16 sticky top-0">
      <div className="container mx-auto px-4 h-full">
        <div className="flex h-full items-center justify-between">
          <nav className="flex w-full gap-4 py-4">
            <ul className="hidden md:flex gap-x-6">
              <li>
                <NavLink className={buttonVariants({ variant: "ghost" })} to="/">Home</NavLink>
              </li>
              <li>
                <NavigationMenu>
                  <NavigationMenuList>
                    <NavigationMenuItem>
                      <NavigationMenuTrigger>NBA</NavigationMenuTrigger>
                      <NavigationMenuContent>
                        <NavLink to="/players">
                          <NavigationMenuLink className={navigationMenuTriggerStyle()}>
                            Players
                          </NavigationMenuLink>
                        </NavLink>
                      </NavigationMenuContent>
                    </NavigationMenuItem>
                  </NavigationMenuList>
                </NavigationMenu>
              </li>
            </ul>
          </nav>
        </div>
      </div>
    </div>
  );
}
