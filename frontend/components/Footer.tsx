"use client";

import React from "react";
import { useLanguage } from "@/context/LanguageContext";
import { Shield, Mail, ArrowUpRight, HeartHandshake } from "lucide-react";

export const Footer: React.FC = () => {
  const { t } = useLanguage();

  return (
    <footer id="contacto" className="bg-slate-950 text-slate-400 py-20 border-t border-slate-900 relative">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        {/* Contact CTA Box */}
        <div className="rounded-3xl bg-gradient-to-r from-medical-darkBlue to-slate-900 p-8 sm:p-12 border border-blue-900/50 shadow-2xl mb-16 text-center max-w-4xl mx-auto">
          <div className="w-12 h-12 rounded-2xl bg-sky-500/20 text-sky-400 flex items-center justify-center mx-auto mb-4">
            <HeartHandshake className="w-6 h-6" />
          </div>
          <h3 className="text-2xl sm:text-3xl font-extrabold text-white mb-3 tracking-tight">
            {t.footer.ctaCardTitle}
          </h3>
          <p className="text-slate-300 text-sm sm:text-base max-w-xl mx-auto mb-8">
            {t.footer.ctaCardSubtitle}
          </p>
          <a
            href="mailto:demo@saferx.ai"
            className="inline-flex items-center justify-center gap-2.5 bg-gradient-to-r from-medical-blue to-sky-600 hover:from-blue-700 hover:to-sky-500 text-white font-bold px-8 py-4 rounded-full transition-all shadow-lg shadow-sky-900/40 hover:scale-105"
          >
            <Mail className="w-5 h-5" />
            <span>{t.footer.contactBtn}</span>
            <ArrowUpRight className="w-4 h-4 opacity-70" />
          </a>
        </div>

        {/* Main Footer Links & Branding */}
        <div className="flex flex-col md:flex-row items-center justify-between gap-8 pb-12 border-b border-slate-900 text-center md:text-left">
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 rounded-xl bg-sky-500/20 text-sky-400 flex items-center justify-center">
              <Shield className="w-5 h-5" />
            </div>
            <div>
              <span className="font-bold text-xl text-white tracking-tight">
                SafeRx <span className="text-sky-400">AI</span>
              </span>
              <span className="block text-xs text-slate-500 font-mono">
                Clinical Pharmacological Intelligence
              </span>
            </div>
          </div>

          <p className="max-w-md text-xs sm:text-sm text-slate-500">
            {t.footer.tagline}
          </p>
        </div>

        {/* Bottom copyright & legal links */}
        <div className="pt-8 flex flex-col sm:flex-row items-center justify-between gap-4 text-xs text-slate-600">
          <p>{t.footer.rights}</p>
          <div className="flex items-center space-x-6">
            <a href="#" className="hover:text-slate-400 transition-colors">
              {t.footer.privacy}
            </a>
            <a href="#" className="hover:text-slate-400 transition-colors">
              {t.footer.terms}
            </a>
            <a href="#" className="hover:text-slate-400 transition-colors">
              {t.footer.security}
            </a>
          </div>
        </div>
      </div>
    </footer>
  );
};
