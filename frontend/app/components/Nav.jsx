import { NavLink } from "@remix-run/react";

export default function Nav() {
  return (
    <nav className="flex gap-4">
      <NavLink
        to="/"
        className={({ isActive }) => (isActive ? "font-bold" : "")}
      >
        Home
      </NavLink>
      <NavLink
        to="/players"
        className={({ isActive }) => (isActive ? "font-bold" : "")}
      >
        Players
      </NavLink>
    </nav>
  );
}
