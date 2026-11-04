/**
 * Virtual Doctor Copilot Embeddable Widget SDK
 * Version: 0.1.0
 * Lightweight, zero-dependency widget for embedding clinical triage & symptom checking
 * into hospital websites, patient portals, or OPD reception kiosks.
 */

(function () {
  const DEFAULT_CONFIG = {
    apiBase: "http://localhost:8010",
    themeColor: "#53172a",
    hospitalName: "Hospital Virtual Doctor Copilot",
    position: "bottom-right", // 'bottom-right' | 'bottom-left' | 'inline'
    targetElementId: null,
  };

  class VirtualDoctorWidget {
    constructor(config = {}) {
      this.config = { ...DEFAULT_CONFIG, ...config };
      this.isOpen = false;
      this.sessionId = null;
      this.step = 0; // 0: Init demographics, 1: Conversation turns
      this.formData = {
        age: 35,
        gender: "female",
        chronic_conditions: "",
      };
      this.init();
    }

    init() {
      this.injectStyles();
      this.createWidgetDOM();
      this.bindEvents();
    }

    injectStyles() {
      if (document.getElementById("vd-widget-styles")) return;
      const style = document.createElement("style");
      style.id = "vd-widget-styles";
      style.innerHTML = `
        .vd-launcher-btn {
          position: fixed;
          bottom: 24px;
          right: 24px;
          z-index: 999999;
          background: ${this.config.themeColor};
          color: #ffffff;
          border: none;
          border-radius: 9999px;
          padding: 14px 22px;
          font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
          font-size: 14px;
          font-weight: 700;
          box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.25);
          cursor: pointer;
          display: flex;
          align-items: center;
          gap: 10px;
          transition: transform 0.2s ease, box-shadow 0.2s ease;
        }
        .vd-launcher-btn:hover {
          transform: translateY(-2px);
          box-shadow: 0 15px 30px -5px rgba(0, 0, 0, 0.35);
        }
        .vd-modal-container {
          position: fixed;
          bottom: 84px;
          right: 24px;
          width: 420px;
          max-width: calc(100vw - 32px);
          height: 620px;
          max-height: calc(100vh - 120px);
          z-index: 999999;
          background: #FFFDF9;
          border: 1px solid #E8D5C4;
          border-radius: 20px;
          box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.35);
          display: none;
          flex-direction: column;
          overflow: hidden;
          font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        }
        .vd-modal-header {
          background: ${this.config.themeColor};
          color: #fff;
          padding: 16px 20px;
          display: flex;
          align-items: center;
          justify-content: space-between;
        }
        .vd-modal-header h3 {
          margin: 0;
          font-size: 15px;
          font-weight: 700;
        }
        .vd-modal-header p {
          margin: 2px 0 0;
          font-size: 11px;
          opacity: 0.85;
        }
        .vd-close-btn {
          background: transparent;
          border: none;
          color: #fff;
          font-size: 20px;
          cursor: pointer;
          padding: 4px 8px;
          border-radius: 6px;
        }
        .vd-modal-body {
          flex: 1;
          padding: 20px;
          overflow-y: auto;
          font-size: 13px;
          color: #292524;
        }
        .vd-form-group {
          margin-bottom: 14px;
        }
        .vd-form-group label {
          display: block;
          font-size: 11px;
          font-weight: 600;
          text-transform: uppercase;
          color: #78716c;
          margin-bottom: 4px;
        }
        .vd-input, .vd-select, .vd-textarea {
          width: 100%;
          box-sizing: border-box;
          padding: 10px 12px;
          border: 1px solid #E8D5C4;
          border-radius: 10px;
          font-size: 13px;
          background: #fff;
          color: #1c1917;
          outline: none;
        }
        .vd-input:focus, .vd-textarea:focus {
          border-color: ${this.config.themeColor};
        }
        .vd-btn-primary {
          background: ${this.config.themeColor};
          color: #fff;
          border: none;
          border-radius: 10px;
          padding: 12px;
          font-size: 13px;
          font-weight: 700;
          cursor: pointer;
          width: 100%;
          margin-top: 10px;
        }
        .vd-alert-card {
          padding: 14px;
          border-radius: 12px;
          margin-bottom: 14px;
        }
        .vd-alert-red {
          background: #FEF2F2;
          border: 1px solid #FCA5A5;
          color: #991B1B;
        }
        .vd-alert-green {
          background: #F0FDF4;
          border: 1px solid #86EFAC;
          color: #166534;
        }
        .vd-soap-box {
          background: #FAF8F5;
          border: 1px solid #E8D5C4;
          border-radius: 10px;
          padding: 12px;
          margin-top: 12px;
        }
        .vd-soap-box h4 {
          margin: 0 0 6px;
          font-size: 12px;
          font-weight: 700;
          color: ${this.config.themeColor};
        }
        .vd-diff-item {
          background: #fff;
          border: 1px solid #E8D5C4;
          border-radius: 8px;
          padding: 10px;
          margin-top: 8px;
        }
      `;
      document.head.appendChild(style);
    }

    createWidgetDOM() {
      // Launcher button
      this.launcher = document.createElement("button");
      this.launcher.className = "vd-launcher-btn";
      this.launcher.innerHTML = `
        <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2.2">
          <path d="M12 2v20M2 12h20M4.93 4.93l14.14 14.14M4.93 19.07l14.14-14.14"/>
        </svg>
        <span>Virtual Doctor</span>
      `;
      document.body.appendChild(this.launcher);

      // Modal container
      this.modal = document.createElement("div");
      this.modal.className = "vd-modal-container";
      this.modal.innerHTML = `
        <div class="vd-modal-header">
          <div>
            <h3>${this.config.hospitalName}</h3>
            <p>Clinical AI Triage &amp; Symptom Copilot</p>
          </div>
          <button class="vd-close-btn" id="vd-close">&times;</button>
        </div>
        <div class="vd-modal-body" id="vd-body">
          ${this.renderStep1()}
        </div>
      `;
      document.body.appendChild(this.modal);
    }

    renderStep1() {
      return `
        <div style="margin-bottom: 16px;">
          <h4 style="margin: 0 0 4px; font-size: 14px; font-weight: 700; color: #1c1917;">1. Patient Demographics</h4>
          <p style="margin: 0; font-size: 12px; color: #78716c;">Basic profile to calibrate clinical age-risk stratification.</p>
        </div>
        <div class="vd-form-group">
          <label>Age in Years *</label>
          <input type="number" id="vd-age" class="vd-input" value="${this.formData.age}" min="0" max="120" required />
        </div>
        <div class="vd-form-group">
          <label>Biological Gender *</label>
          <select id="vd-gender" class="vd-select">
            <option value="female" ${this.formData.gender === "female" ? "selected" : ""}>Female</option>
            <option value="male" ${this.formData.gender === "male" ? "selected" : ""}>Male</option>
            <option value="other" ${this.formData.gender === "other" ? "selected" : ""}>Other</option>
          </select>
        </div>
        <div class="vd-form-group">
          <label>Known Chronic Illnesses (Optional)</label>
          <input type="text" id="vd-chronic" class="vd-input" placeholder="e.g. Hypertension, Diabetes, Asthma, CAD" value="${this.formData.chronic_conditions}" />
        </div>
        <button class="vd-btn-primary" id="vd-next-step-1">Continue to Symptoms &rarr;</button>
      `;
    }

    renderStep2() {
      return `
        <div style="margin-bottom: 16px;">
          <h4 style="margin: 0 0 4px; font-size: 14px; font-weight: 700; color: #1c1917;">2. Describe Symptoms (OPQRST)</h4>
          <p style="margin: 0; font-size: 12px; color: #78716c;">Explain your primary discomfort in your own words.</p>
        </div>
        <div class="vd-form-group">
          <label>Chief Complaint *</label>
          <textarea id="vd-complaint" rows="2" class="vd-textarea" placeholder="e.g. Burning chest discomfort after meals, or throbbing headache" required>${this.formData.chief_complaint}</textarea>
        </div>
        <div class="vd-form-group">
          <label>Onset / Duration</label>
          <input type="text" id="vd-onset" class="vd-input" placeholder="e.g. Started suddenly 2 hours ago / 3 days" value="${this.formData.onset}" />
        </div>
        <div class="vd-form-group">
          <label>Quality / Character</label>
          <input type="text" id="vd-quality" class="vd-input" placeholder="e.g. Sharp, dull aching, burning, throbbing" value="${this.formData.quality_character}" />
        </div>
        <div class="vd-form-group">
          <label>Severity (1 to 10 Scale)</label>
          <input type="range" id="vd-severity" min="1" max="10" value="${this.formData.severity_scale}" style="width: 100%;" />
          <div style="display: flex; justify-content: space-between; font-size: 11px; color: #78716c;">
            <span>1 (Mild)</span>
            <span id="vd-severity-val">5 / 10</span>
            <span>10 (Severe)</span>
          </div>
        </div>
        <div class="vd-form-group">
          <label>Associated Symptoms (Comma separated)</label>
          <input type="text" id="vd-associated" class="vd-input" placeholder="e.g. Fever, nausea, dizziness" value="${this.formData.associated_symptoms}" />
        </div>
        <div style="display: flex; gap: 8px; margin-top: 10px;">
          <button style="width: 35%; background: #e7e5e4; border: none; border-radius: 10px; cursor: pointer; font-weight: 600;" id="vd-back-step-2">&larr; Back</button>
          <button style="width: 65%;" class="vd-btn-primary" id="vd-submit-assessment">Analyze Symptoms &rarr;</button>
        </div>
      `;
    }

    renderLoading() {
      return `
        <div style="text-align: center; padding: 40px 20px;">
          <div style="display: inline-block; width: 40px; height: 40px; border: 4px solid #E8D5C4; border-top-color: ${this.config.themeColor}; border-radius: 50%; animation: vd-spin 0.8s linear infinite;"></div>
          <style>@keyframes vd-spin { to { transform: rotate(360deg); } }</style>
          <h4 style="margin: 16px 0 6px; font-size: 15px; color: #1c1917;">Evaluating Clinical Guidelines...</h4>
          <p style="margin: 0; font-size: 12px; color: #78716c;">Running Red-Flag triage, vector retrieval, and ICD-10 diagnostic matching.</p>
        </div>
      `;
    }

    renderAssessment(data) {
      const isRedFlag = data.triage_level === "EMERGENCY_RED";

      let html = "";

      if (isRedFlag) {
        html += `
          <div class="vd-alert-card vd-alert-red">
            <h4 style="margin: 0 0 6px; font-weight: 800; font-size: 14px;">🚨 IMMEDIATE EMERGENCY ALERT</h4>
            <p style="margin: 0 0 8px; font-size: 12px; line-height: 1.4;">${data.red_flag_alert.urgency_recommendation}</p>
            <a href="tel:${data.red_flag_alert.emergency_call_action}" style="display: inline-block; background: #DC2626; color: #fff; padding: 8px 16px; border-radius: 8px; text-decoration: none; font-weight: 800; font-size: 12px;">CALL 108 IMMEDIATELY</a>
          </div>
        `;
      } else {
        html += `
          <div class="vd-alert-card vd-alert-green">
            <h4 style="margin: 0 0 4px; font-weight: 700; font-size: 13px;">Triage Level: ${data.triage_level}</h4>
            <p style="margin: 0; font-size: 12px;">Recommended Clinic: <strong>${data.recommended_specialty_clinic}</strong></p>
          </div>
        `;
      }

      html += `
        <div style="margin-top: 14px;">
          <h4 style="margin: 0 0 6px; font-size: 13px; font-weight: 700;">Differential Considerations:</h4>
      `;

      data.differential_diagnoses.forEach((d) => {
        html += `
          <div class="vd-diff-item">
            <div style="display: flex; justify-content: space-between; align-items: baseline;">
              <strong style="color: #1c1917; font-size: 13px;">${d.probability_rank}. ${d.diagnosis_name}</strong>
              <span style="font-family: monospace; font-size: 11px; background: #f5f5f4; padding: 2px 6px; border-radius: 4px;">${d.icd10_code || "ICD-10"}</span>
            </div>
            <p style="margin: 4px 0 0; font-size: 12px; color: #57534e; line-height: 1.35;">${d.clinical_rationale}</p>
          </div>
        `;
      });

      html += `
        </div>
        <div class="vd-soap-box">
          <h4>Clinical Summary (Physician Handoff)</h4>
          <p style="margin: 0 0 6px; font-size: 11px; color: #44403c;"><strong>Subjective:</strong> ${data.soap_note.subjective}</p>
          <p style="margin: 0 0 6px; font-size: 11px; color: #44403c;"><strong>Assessment:</strong> ${data.soap_note.assessment}</p>
          <p style="margin: 0; font-size: 11px; color: #44403c;"><strong>Plan:</strong> ${data.soap_note.plan.replace(/\n/g, "<br/>")}</p>
        </div>
        <button class="vd-btn-primary" id="vd-start-new" style="margin-top: 14px;">Start New Consultation</button>
      `;

      return html;
    }

    renderChatContainer(firstGreeting, firstQuestion) {
      return `
        <div class="vd-chat-messages" id="vd-chat-msgs" style="display: flex; flex-direction: column; gap: 10px; margin-bottom: 14px; max-height: 400px; overflow-y: auto;">
          <div style="background: #FAF8F5; border: 1px solid #E8D5C4; border-radius: 12px; padding: 10px 14px; font-size: 12px; color: #44403c;">
            <strong>Virtual Doctor Copilot:</strong><br/>
            ${firstGreeting}
          </div>
          <div style="background: #FAF8F5; border: 1px solid #E8D5C4; border-radius: 12px; padding: 10px 14px; font-size: 13px; font-weight: 600; color: #1c1917;">
            ${firstQuestion}
          </div>
        </div>
        <div id="vd-chat-input-area" style="display: flex; gap: 8px;">
          <input type="text" id="vd-user-input" class="vd-input" placeholder="Type your answer here..." style="flex: 1;" />
          <button class="vd-btn-primary" id="vd-send-msg" style="width: auto; padding: 0 16px; margin: 0;">Send</button>
        </div>
      `;
    }

    bindEvents() {
      this.launcher.addEventListener("click", () => this.toggleModal());
      document.getElementById("vd-close").addEventListener("click", () => this.toggleModal());

      const body = document.getElementById("vd-body");

      body.addEventListener("click", async (e) => {
        if (e.target && e.target.id === "vd-next-step-1") {
          this.formData.age = parseInt(document.getElementById("vd-age").value) || 35;
          this.formData.gender = document.getElementById("vd-gender").value;
          this.formData.chronic_conditions = document.getElementById("vd-chronic").value;
          body.innerHTML = this.renderLoading();

          try {
            const initRes = await fetch(`${this.config.apiBase}/api/v1/session/start`, {
              method: "POST",
              headers: { "Content-Type": "application/json" },
              body: JSON.stringify({
                patient: {
                  age: this.formData.age,
                  gender: this.formData.gender,
                  chronic_conditions: this.formData.chronic_conditions
                    ? this.formData.chronic_conditions.split(",").map((s) => s.trim()).filter(Boolean)
                    : [],
                },
                language_preference: "en",
              }),
            });
            const initData = await initRes.json();
            this.sessionId = initData.session_id;
            body.innerHTML = this.renderChatContainer(initData.greeting, initData.next_question);
            this.bindChatEvents();
          } catch (err) {
            body.innerHTML = `<div style="color: #991b1b; padding: 20px; text-align: center;">Error: ${err.message}</div>`;
          }
        }
      });
    }

    bindChatEvents() {
      const input = document.getElementById("vd-user-input");
      const sendBtn = document.getElementById("vd-send-msg");
      const msgContainer = document.getElementById("vd-chat-msgs");

      const handleSend = async () => {
        const text = input.value.trim();
        if (!text) return;
        input.value = "";

        // Append patient message
        const pBubble = document.createElement("div");
        pBubble.style.cssText = "align-self: flex-end; background: #53172a; color: #fff; border-radius: 12px; padding: 10px 14px; font-size: 13px; max-width: 80%;";
        pBubble.innerText = text;
        msgContainer.appendChild(pBubble);
        msgContainer.scrollTop = msgContainer.scrollHeight;

        try {
          const res = await fetch(`${this.config.apiBase}/api/v1/session/${this.sessionId}/message`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message: text }),
          });
          const data = await res.json();

          if (data.is_complete && data.final_assessment) {
            const body = document.getElementById("vd-body");
            body.innerHTML = this.renderAssessment(data.final_assessment);
            document.getElementById("vd-start-new").addEventListener("click", () => {
              body.innerHTML = this.renderStep1();
            });
          } else {
            // Append doctor question
            const dBubble = document.createElement("div");
            dBubble.style.cssText = "background: #FAF8F5; border: 1px solid #E8D5C4; border-radius: 12px; padding: 10px 14px; font-size: 13px; font-weight: 600; color: #1c1917; max-width: 90%;";
            dBubble.innerText = data.reply_text;
            msgContainer.appendChild(dBubble);
            msgContainer.scrollTop = msgContainer.scrollHeight;
          }
        } catch (err) {
          alert("Error: " + err.message);
        }
      };

      sendBtn.addEventListener("click", handleSend);
      input.addEventListener("keydown", (e) => {
        if (e.key === "Enter") handleSend();
      });
    }

    toggleModal() {
      this.isOpen = !this.isOpen;
      this.modal.style.display = this.isOpen ? "flex" : "none";
    }
  }

  // Expose globally
  window.VirtualDoctorWidget = VirtualDoctorWidget;
})();
