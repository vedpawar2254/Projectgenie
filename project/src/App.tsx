import React from 'react';
import { Wand2, Brain, Rocket, Github, ExternalLink, MessageCircleQuestion, ChevronRight, Star } from 'lucide-react';

function App() {
  return (
    <div className="min-h-screen bg-black text-white">
      {/* Navigation */}
      <nav className="fixed w-full z-50 glass-card">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between h-16 items-center">
            <div className="flex items-center space-x-2">
              <Wand2 className="h-6 w-6 text-purple-400" />
              <span className="text-xl font-bold text-white">Project Genie</span>
            </div>
            <div className="hidden md:flex space-x-8">
              <a href="#about" className="text-gray-300 hover:text-white transition-colors">About</a>
              <a href="#features" className="text-gray-300 hover:text-white transition-colors">Features</a>
              <a href="#faq" className="text-gray-300 hover:text-white transition-colors">FAQ</a>
            </div>
          </div>
        </div>
      </nav>

      {/* Hero Section */}
      <section className="relative animate-gradient">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pt-32 pb-40">
          <div className="text-center relative z-10">
            <div className="inline-flex items-center space-x-2 px-4 py-2 rounded-full bg-white/10 backdrop-blur-sm mb-8">
              <Star className="h-4 w-4 text-yellow-400" />
              <span className="text-sm">Your AI-Powered Career Guide</span>
            </div>
            <h1 className="text-5xl md:text-7xl font-bold mb-8 leading-tight">
              Transform Your <span className="rainbow-text">Learning Journey</span>
            </h1>
            <p className="text-xl md:text-2xl text-gray-300 mb-12 max-w-3xl mx-auto">
              Let AI guide your path to becoming an exceptional developer with personalized roadmaps and project ideas.
            </p>
            <div className="flex flex-col sm:flex-row gap-4 justify-center items-center">
              <a
                href="https://project-genie.streamlit.app/"
                target="_blank"
                rel="noopener noreferrer"
                className="inline-flex items-center px-8 py-4 rounded-full bg-white text-black font-semibold hover:bg-gray-100 transition-colors"
              >
                Get Started <ChevronRight className="ml-2 h-5 w-5" />
              </a>
              <a href="#demo" className="inline-flex items-center px-8 py-4 rounded-full border border-white/20 hover:bg-white/10 transition-colors">
                View Demo
              </a>
            </div>
          </div>
        </div>
        <div className="absolute inset-0 bg-[url('https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&q=80')] opacity-10 mix-blend-overlay"></div>
      </section>

      {/* Features Section */}
      <section id="features" className="py-32 bg-black relative">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-20">
            <h2 className="text-4xl font-bold mb-4">Unlock Your Potential</h2>
            <p className="text-gray-400 text-lg">Discover what Project Genie can do for your development journey</p>
          </div>
          <div className="grid md:grid-cols-3 gap-8">
            <div className="glass-card rounded-2xl p-8 transform hover:scale-105 transition-transform">
              <Brain className="h-12 w-12 text-purple-400 mb-6" />
              <h3 className="text-xl font-semibold mb-4">Smart Analysis</h3>
              <p className="text-gray-400">Our AI analyzes your resume to understand your current skill set and experience level, providing tailored recommendations.</p>
            </div>
            <div className="glass-card rounded-2xl p-8 transform hover:scale-105 transition-transform">
              <Wand2 className="h-12 w-12 text-purple-400 mb-6" />
              <h3 className="text-xl font-semibold mb-4">Personalized Roadmap</h3>
              <p className="text-gray-400">Get a customized learning path that adapts to your goals and current expertise level.</p>
            </div>
            <div className="glass-card rounded-2xl p-8 transform hover:scale-105 transition-transform">
              <Rocket className="h-12 w-12 text-purple-400 mb-6" />
              <h3 className="text-xl font-semibold mb-4">Project Ideas</h3>
              <p className="text-gray-400">Receive curated project suggestions that help you practice and showcase your growing skills.</p>
            </div>
          </div>
        </div>
      </section>

      {/* Demo Section */}
      <section id="demo" className="py-32 bg-gradient-to-b from-black to-purple-900/20">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-16">
            <h2 className="text-4xl font-bold mb-4">See It In Action</h2>
            <p className="text-gray-400 text-lg">Watch how Project Genie transforms your career path</p>
          </div>
          <div className="rounded-2xl overflow-hidden shadow-2xl border border-purple-500/20">
            <img
              src="https://images.unsplash.com/photo-1555066931-4365d14bab8c?auto=format&fit=crop&w=1200&q=80"
              alt="Project Genie Demo"
              className="w-full object-cover transform hover:scale-105 transition-transform duration-700"
            />
          </div>
        </div>
      </section>

      {/* FAQ Section */}
      <section id="faq" className="py-32 bg-black">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-20">
            <h2 className="text-4xl font-bold mb-4">Frequently Asked Questions</h2>
            <p className="text-gray-400 text-lg">Everything you need to know about Project Genie</p>
          </div>
          <div className="grid md:grid-cols-2 gap-8">
            <div className="glass-card rounded-2xl p-8">
              <MessageCircleQuestion className="h-8 w-8 text-purple-400 mb-4" />
              <h3 className="text-xl font-semibold mb-4">How does Project Genie work?</h3>
              <p className="text-gray-400">Simply upload your resume and tell us what you want to learn. Our AI analyzes your profile to create a personalized learning roadmap with project suggestions tailored to your goals.</p>
            </div>
            <div className="glass-card rounded-2xl p-8">
              <MessageCircleQuestion className="h-8 w-8 text-purple-400 mb-4" />
              <h3 className="text-xl font-semibold mb-4">Is it free to use?</h3>
              <p className="text-gray-400">Yes, Project Genie is completely free to use. We believe in making career guidance accessible to everyone who wants to grow in their development journey.</p>
            </div>
          </div>
        </div>
      </section>

      {/* Built By Section */}
      <footer className="py-16 bg-black border-t border-white/10">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <p className="text-gray-400 mb-4">Built with ❤️ by Ved</p>
          <div className="flex justify-center space-x-4">
            <a
              href="https://github.com/vedpawar2254"
              target="_blank"
              rel="noopener noreferrer"
              className="text-gray-400 hover:text-white transition-colors"
            >
              <Github className="h-6 w-6" />
            </a>
          </div>
        </div>
      </footer>
    </div>
  );
}

export default App;