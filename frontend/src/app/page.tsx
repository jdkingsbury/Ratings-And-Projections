import { buttonVariants } from "@/components/ui/button";
import { PlayerCardInfo } from "./types";
import axios from "axios";
import { BACKEND_API_BASE_URL } from "@/components/utils/constants";
import PlayerCard from "@/components/player-card";

type FetchPlayerCardInfo = {
  data: PlayerCardInfo | null;
  error: string | null;
};

async function fetchPlayerCardInfo(): Promise<FetchPlayerCardInfo> {
  try {
    const response = await axios.get<PlayerCardInfo>(
      `${BACKEND_API_BASE_URL}/nba/players/1628973/player_card`,
    );
    return { error: null, data: response.data };
  } catch (error: any) {
    console.error(`Failed to fetch player card info: ${error.message}`);
    return { error: error.message, data: null };
  }
}

export default async function Home() {
  const { data: player, error } = await fetchPlayerCardInfo();

  return (
    <div className="flex min-h-screen flex-col bg-background">
      <main className="flex-1">
        <section className="container mx-auto flex flex-col items-center justify-center gap-6 px-4 py-12 md:py-24">
          <div className="text-center">
            <h1 className="text-3xl font-bold tracking-tighter sm:text-4xl md:text-5xl animate-fadeIn">
              Ratings and Projections
            </h1>
            <p className="mt-4 text-lg sm:text-xl md:text-2xl text-muted-foreground">
              Discover the top-rated teams and players and their future
              projections
            </p>
          </div>
        </section>
        <section className="container mx-auto px-4 py-12">
          <div className="p-6 md:p-8 rounded-lg">
            <div className="text-center mb-6">
              <p className="text-2xl font-bold tracking-tighter sm:text-xl md:text-2xl">
                Top Player Ratings
              </p>
            </div>
            <div className="flex flex-col items-center">
              {error ? (
                <p className="text-red-500">
                  Error when fetching player card info: {error}
                </p>
              ) : !player ? (
                <p className="text-gray-500">Player not found.</p>
              ) : (
                <PlayerCard player={player} />
              )}
            </div>
          </div>
        </section>
      </main>
      <footer className="py-6">
        <div className="container mx-auto flex md:flex-row items-center justify-between text-sm">
          <div className="flex gap-4 mb-4 md:mb-0">
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
        </div>
      </footer>
    </div>
  );
}
