export default async function AboutMe() {
  return (
    <div className="flex flex-col min-h-screen bg-background">
      <main className="flex-1">
        <section className="container mx-auto flex flex-col">
          <h1 className="text-2xl font-semibold tracking-tighter sm:text-3xl md:text-4xl">
            About Me
          </h1>
          <p className="mt-4 text-lg sm:text-xl md:text-2xl">
            The purpose for creating the applications was to create a fun site to create player ratings for players similar to 2k.
            The player grades are determined by player performance per game. 

            The Goal is to be able to show accurate player ratings and show the projections and performance overtime.
          </p>
        </section>
      </main>
    </div>
  );
}
