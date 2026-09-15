import { Navbar } from "@/components/Navbar";
import { Hero } from "@/components/Hero";
import { ProblemBento } from "@/components/ProblemBento";
import { SolutionShowcase } from "@/components/SolutionShowcase";
import { ComplianceSection } from "@/components/ComplianceSection";
import { TargetAudience } from "@/components/TargetAudience";
import { Footer } from "@/components/Footer";

export default function Home() {
  return (
    <main className="min-h-screen bg-white">
      <Navbar />
      <Hero />
      <ProblemBento />
      <SolutionShowcase />
      <ComplianceSection />
      <TargetAudience />
      <Footer />
    </main>
  );
}
