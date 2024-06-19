import { Link } from "@remix-run/react";
import Nav from "../components/Nav";

export default function Index() {
  return (
    <div>
      <Nav />
      <h1 className="text-3xl font-mono">Home</h1>
      <Link to="/players">View Player Stats</Link>
    </div>
  );
}
