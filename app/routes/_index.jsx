import { Link } from "@remix-run/react";

export default function Index() {
  return (
    <div>
      <h1 className="text-3xl font-mono">Home</h1>
      <Link to="/players">View Player Stats</Link>
    </div>
  );
}
