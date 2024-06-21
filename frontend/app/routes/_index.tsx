import { Link } from "@remix-run/react";
import Navbar from "~/components/navigation/navbar";
import { Button } from "~/components/ui/button";

export default function Index() {
  return (
    <div>
      <Navbar />
      <h1 className="text-3xl font-mono">Home</h1>
      <Button>Click me</Button>
    </div>
  );
}
