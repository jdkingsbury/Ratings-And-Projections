import { Button } from "@/components/ui/button";
import Navbar from "@/components/navbar-menu";

export default function Home() {
  return (
    <div className="flex min-h-[100dvh] flex-col bg-background">
      <main className="flex-1">
        <section className="container mx-auto flex flex-col items-center justify-center gap-6 px-4 py-12 md:py-24">
          <div className="text-center">
            <h1 className="text-3xl font-bold tracking-tighter sm:text-4xl md:text-5xl">
              Ratings and Projections
            </h1>
          </div>
        </section>
      </main>
      <footer className="bg-muted py-6 text-center text-sm text-muted-foreground">
        <div className="container mx-auto px-4">
          &copy; 2024 Sports Predictions. All rights reserved.
        </div>
      </footer>
    </div>
  );
}
