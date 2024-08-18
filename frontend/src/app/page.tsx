import { buttonVariants } from "@/components/ui/button";
import Navbar from "@/components/navbar-menu";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";

export default function Home() {
  return (
    <div className="flex min-h-[100dvh] flex-col bg-background">
      <main className="flex-1">
        <section className="container mx-auto flex flex-col items-center justify-center gap-6 px-4 py-12 md:py-24">
          <div className="text-center">
            <h1 className="text-3xl font-bold tracking-tighter sm:text-4xl md:text-5xl animate-fadeIn">
              Ratings and Projections
            </h1>
            <p className="mt-4 text-lg sm:text-xl md:text-2xl text-muted-foreground">
              Fun site for rating teams and players and showing their future
              projections
            </p>
          </div>
        </section>
        <section className="container mx-auto px-4 py-12">
          <Card className="p-8 rounded-lg shadow-lg">
            <CardHeader className="text-2xl font-bold text-center">
              <CardTitle className="text-2xl font-bold tracking-tighter text-center">
                See How It Works
              </CardTitle>
            </CardHeader>
            <CardContent className="flex flex-col items-center">
              <p className="text-lg mb-4">Checkout Sample Rating Below:</p>
              <div className="bg-muted p-4 rounded-lg text-center">
                <p className="text-xl font-bold">Team A: 85</p>
              </div>
            </CardContent>
          </Card>
        </section>
      </main>
      <footer className="container mx-auto flex items-center justify-between py-6 text-sm text-muted-foreground">
        <div className="flex gap-4">
          <a
            href="/privacy-policy"
            className={buttonVariants({ variant: "ghost" })}
          >
            Privacy Policy
          </a>
          <a
            href="/terms-of-service"
            className={buttonVariants({ variant: "ghost" })}
          >
            Terms of Service
          </a>
        </div>
        <p>&copy; 2024 Sports Predictions. All rights reserved.</p>
      </footer>
    </div>
  );
}
