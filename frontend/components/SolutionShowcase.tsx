"use client";

import React, { useState } from "react";
import { useLanguage } from "@/context/LanguageContext";
import {
  Cpu,
  CheckCircle2,
  AlertOctagon,
  XCircle,
  Sparkles,
  Search,
  User,
  Activity,
  ArrowRight,
  RefreshCw,
} from "lucide-react";

export const SolutionShowcase: React.FC = () => {
  const { t } = useLanguage();
  const [prescriptionCancelled, setPrescriptionCancelled] = useState(false);
  const [showAlternatives, setShowAlternatives] = useState(false);

  return (
    <section
      id="solucion"
      className="py-24 bg-gradient-to-b from-gray-50 via-medical-softBlue/40 to-gray-50 relative overflow-hidden"
    >
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="lg:grid lg:grid-cols-12 lg:gap-16 items-center">
          {/* Left Column: Solution narrative */}
          <div className="lg:col-span-5 mb-14 lg:mb-0">
            <div className="inline-flex items-center gap-2 px-3 py-1 rounded-md bg-emerald-50 border border-emerald-100 text-medical-green text-xs font-bold uppercase tracking-wider mb-4">
              <Cpu className="w-3.5 h-3.5" />
              <span>{t.solution.tag}</span>
            </div>
            <h2 className="text-3xl sm:text-4xl font-extrabold text-medical-navy tracking-tight leading-tight">
              {t.solution.title}
            </h2>
            <p className="mt-5 text-base sm:text-lg text-gray-600 leading-relaxed">
              {t.solution.subtitle}
            </p>

            <div className="mt-8 space-y-5">
              <div className="flex items-start gap-3.5">
                <div className="w-6 h-6 rounded-full bg-emerald-100 flex items-center justify-center text-emerald-600 flex-shrink-0 mt-0.5">
                  <CheckCircle2 className="w-4 h-4" />
                </div>
                <div>
                  <h4 className="text-base font-bold text-gray-900">
                    {t.solution.benefit1Title}
                  </h4>
                  <p className="text-sm text-gray-500 mt-0.5">
                    {t.solution.benefit1Desc}
                  </p>
                </div>
              </div>

              <div className="flex items-start gap-3.5">
                <div className="w-6 h-6 rounded-full bg-emerald-100 flex items-center justify-center text-emerald-600 flex-shrink-0 mt-0.5">
                  <CheckCircle2 className="w-4 h-4" />
                </div>
                <div>
                  <h4 className="text-base font-bold text-gray-900">
                    {t.solution.benefit2Title}
                  </h4>
                  <p className="text-sm text-gray-500 mt-0.5">
                    {t.solution.benefit2Desc}
                  </p>
                </div>
              </div>

              <div className="flex items-start gap-3.5">
                <div className="w-6 h-6 rounded-full bg-emerald-100 flex items-center justify-center text-emerald-600 flex-shrink-0 mt-0.5">
                  <CheckCircle2 className="w-4 h-4" />
                </div>
                <div>
                  <h4 className="text-base font-bold text-gray-900">
                    {t.solution.benefit3Title}
                  </h4>
                  <p className="text-sm text-gray-500 mt-0.5">
                    {t.solution.benefit3Desc}
                  </p>
                </div>
              </div>
            </div>
          </div>

          {/* Right Column: Realistic EHR Simulator Mockup */}
          <div className="lg:col-span-7">
            <div className="relative rounded-3xl bg-white shadow-2xl border border-blue-100/80 overflow-hidden">
              {/* EHR Window Titlebar */}
              <div className="bg-slate-900 px-5 py-3.5 flex items-center justify-between text-white border-b border-slate-800">
                <div className="flex items-center space-x-2">
                  <div className="w-3 h-3 rounded-full bg-red-500/90" />
                  <div className="w-3 h-3 rounded-full bg-amber-500/90" />
                  <div className="w-3 h-3 rounded-full bg-emerald-500/90" />
                </div>
                <div className="flex items-center gap-2 text-xs font-mono text-slate-300">
                  <Activity className="w-3.5 h-3.5 text-emerald-400" />
                  <span>{t.solution.mockup.ehrSystem}</span>
                </div>
                <div className="text-[10px] bg-slate-800 text-slate-400 px-2 py-0.5 rounded font-mono">
                  HL7 FHIR v4
                </div>
              </div>

              {/* Patient Banner */}
              <div className="bg-slate-50 px-6 py-4 border-b border-gray-200 flex flex-wrap items-center justify-between gap-3">
                <div className="flex items-center gap-3">
                  <div className="w-10 h-10 rounded-full bg-medical-blue text-white flex items-center justify-center font-bold text-sm shadow">
                    <User className="w-5 h-5" />
                  </div>
                  <div>
                    <h3 className="font-bold text-gray-900 text-base">
                      {t.solution.mockup.patientName}
                    </h3>
                    <div className="flex items-center gap-2 text-xs text-gray-500">
                      <span>{t.solution.mockup.patientAge}</span>
                      <span>•</span>
                      <span>HC: #894210</span>
                      <span>•</span>
                      <span className="text-emerald-700 bg-emerald-100 px-1.5 py-0.5 rounded font-medium">
                        Riesgo Cardiovascular
                      </span>
                    </div>
                  </div>
                </div>

                <div className="text-right">
                  <span className="text-xs text-gray-400 block">
                    {t.solution.mockup.activeRxLabel}
                  </span>
                  <span className="text-xs font-bold text-medical-navy bg-white px-2.5 py-1 rounded-md border border-gray-200 shadow-sm inline-block mt-0.5">
                    💊 {t.solution.mockup.activeDrug1} ({t.solution.mockup.activeDrug1Dose})
                  </span>
                </div>
              </div>

              {/* Prescription Form Area */}
              <div className="p-6 sm:p-8 space-y-6">
                <div>
                  <div className="flex justify-between items-center mb-2">
                    <label className="text-xs font-bold uppercase tracking-wider text-gray-500">
                      {t.solution.mockup.newRxLabel}
                    </label>
                    <span className="text-xs text-sky-600 font-semibold flex items-center gap-1">
                      <Sparkles className="w-3 h-3" /> SafeRx AI Guardian On
                    </span>
                  </div>

                  {/* Input Simulation */}
                  <div className="flex items-center border-2 border-medical-blue/80 rounded-xl px-4 py-3 bg-white shadow-sm ring-4 ring-blue-50">
                    <Search className="w-5 h-5 text-gray-400 mr-3" />
                    <span className="text-gray-900 font-bold flex-1 text-base">
                      {t.solution.mockup.prescribingDrug}
                    </span>
                    <span className="text-xs bg-blue-100 text-medical-blue font-bold px-2.5 py-1 rounded-md">
                      {t.solution.mockup.prescribingDose}
                    </span>
                  </div>
                </div>

                {/* Simulated Critical Red Alert Banner */}
                {!prescriptionCancelled ? (
                  <div className="bg-red-50 border-2 border-red-500 rounded-2xl p-5 sm:p-6 shadow-glow-danger transition-all duration-300">
                    <div className="flex items-start gap-4">
                      <div className="w-12 h-12 rounded-xl bg-red-600 text-white flex items-center justify-center flex-shrink-0 shadow-md">
                        <AlertOctagon className="w-7 h-7 animate-pulse" />
                      </div>
                      <div className="flex-1">
                        <div className="flex items-center justify-between gap-2 flex-wrap mb-1">
                          <span className="inline-block px-2.5 py-0.5 rounded-full bg-red-600 text-white text-[11px] font-black uppercase tracking-wider">
                            {t.solution.mockup.alertBadge}
                          </span>
                          <span className="text-[11px] text-red-700 font-mono font-semibold">
                            Interacción Farmacodinámica Grave
                          </span>
                        </div>

                        <h4 className="text-base sm:text-lg font-black text-red-900 tracking-tight mt-1">
                          {t.solution.mockup.alertTitle}
                        </h4>

                        <p className="mt-2 text-xs sm:text-sm text-red-800 leading-relaxed font-medium">
                          {t.solution.mockup.alertDesc1}{" "}
                          <strong className="underline decoration-red-400">
                            {t.solution.mockup.alertDrugTaken}
                          </strong>
                          {t.solution.mockup.alertDesc2}{" "}
                          <strong className="underline decoration-red-400">
                            {t.solution.mockup.alertDrugNew}
                          </strong>{" "}
                          {t.solution.mockup.alertDesc3}
                        </p>

                        {showAlternatives && (
                          <div className="mt-4 p-3 bg-white/90 rounded-xl border border-red-200 text-xs text-gray-700 space-y-1">
                            <span className="font-bold text-gray-900 block">
                              Sugerencias de menor interacción gastrointestinal:
                            </span>
                            <p>• Evaluar anticoagulantes orales directos (ACOD) con ajuste de dosis renal.</p>
                            <p>• Considerar gastroprotección estricta si la indicación dual es imperativa.</p>
                          </div>
                        )}

                        {/* Actions buttons */}
                        <div className="mt-5 flex flex-wrap gap-3">
                          <button
                            onClick={() => setPrescriptionCancelled(true)}
                            className="bg-red-600 hover:bg-red-700 text-white text-xs font-bold px-4 py-2.5 rounded-xl shadow transition-all hover:scale-105 flex items-center gap-1.5"
                          >
                            <XCircle className="w-4 h-4" />
                            <span>{t.solution.mockup.actionCancel}</span>
                          </button>
                          <button
                            onClick={() => setShowAlternatives(!showAlternatives)}
                            className="bg-white hover:bg-red-50 text-red-700 border border-red-300 text-xs font-bold px-4 py-2.5 rounded-xl shadow-sm transition-all"
                          >
                            {t.solution.mockup.actionAlternatives}
                          </button>
                        </div>
                      </div>
                    </div>
                  </div>
                ) : (
                  <div className="bg-emerald-50 border-2 border-emerald-500 rounded-2xl p-6 text-center shadow-md">
                    <div className="w-12 h-12 rounded-full bg-emerald-600 text-white flex items-center justify-center mx-auto mb-3">
                      <CheckCircle2 className="w-7 h-7" />
                    </div>
                    <h4 className="text-base font-bold text-emerald-900">
                      Prescripción descartada con éxito
                    </h4>
                    <p className="text-xs sm:text-sm text-emerald-700 mt-1">
                      El paciente permanece seguro sin conflicto farmacológico.
                    </p>
                    <button
                      onClick={() => {
                        setPrescriptionCancelled(false);
                        setShowAlternatives(false);
                      }}
                      className="mt-4 inline-flex items-center gap-1.5 text-xs text-emerald-800 font-bold hover:underline"
                    >
                      <RefreshCw className="w-3.5 h-3.5" />
                      Reiniciar simulación interactiva
                    </button>
                  </div>
                )}
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};
