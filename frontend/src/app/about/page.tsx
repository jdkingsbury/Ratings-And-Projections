export default async function AboutMe() {
  return (
    <div className="flex flex-col min-h-screen bg-background">
      <main className="flex-1 flex justify-center items-center">
        <section className="container mx-auto px-6 py-12 sm:px-12 md:px-20 lg:px-32 text-center">
          <h1 className="text-4xl font-extrabold tracking-tight sm:text-4xl md:text-5xl mb-8 animate-fadeIn">
            About Me
          </h1>
          <div className="border-t border-primary w-32 mx-auto mb-8"> </div>
          <p className="text-xl sm:text-2xl md:text-3xl tracking-tight leading-relaxed mb-12">
            Welcome to Ratings and Projections, The platform designed to create
            player and team ratings based of players performance and how well
            players fit on a team.
          </p>
          <h2 className="text-2xl font-semibold tracking-tight sm:text-3xl md:text-4xl mb-10">
            Why I Created the App
          </h2>
          <p className="text-lg sm:text-xl md:text-2xl tracking-tight leading-relaxed mb-8">
            I am big sports fan and I wanted to create a fun site that will keep
            track of players and teams performances and create ratings for each
            player similar to how 2K creates player ratings or bleacher report
            will grade trades. The player grades are determined by player
            performance per game.
          </p>
          <h2 className="text-2xl font-semibold tracking-tight sm:text-3xl md:text-4xl mb-10">
            Goal of the App
          </h2>
          <p className="text-lg sm:text-xl md:text-2xl tracking-tight leading-relaxed mb-12">
            The Goal is to be able to show accurate player and team ratings and
            show the projections and performance overtime.
          </p>
        </section>
      </main>
      <footer className="text-center py-6 text-muted-foreground">
        © 2024 Ratings and Projections. All rights reserved.
      </footer>
    </div>
  );
}
