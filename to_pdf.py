from weasyprint import HTML, CSS

# The HTML content provided by the user
html_content = """
<html lang="en">
<head>
    <meta charset="UTF-8">
    <style>
        @page {
            size: A4;
            margin: 12px;
        }
        body {
            text-align: justify;
            text-justify: inter-word;
            font-family: "Georgia", serif;
            color: #333;
            font-size: 10.5pt;
            line-height: 1.25;
        }
        .container {
            width: 100%;
        }
        h1 { font-size: 22pt; margin-bottom: 2pt; }
        h3.section-title {
            text-transform: uppercase;
            letter-spacing: 1px;
            font-size: 11pt;
            font-weight: bold;
            color: #222;
            margin-top: 8pt;
            margin-bottom: 2pt;
        }
        h5 { font-size: 11pt; margin-top: 4pt; margin-bottom: 2pt; }
        hr {
            border: 0;
            height: 1.5px;
            background-color: #ccc;
            margin: 2pt 0;
        }
        .d-flex { display: flex; justify-content: space-between; align-items: baseline; }
        .mx-4 { margin-left: 15pt; margin-right: 15pt; }
        ul { margin-top: 2pt; margin-bottom: 4pt; padding-left: 15pt; }
        li { margin-bottom: 2pt; }
        code {
            font-family: monospace;
            color: black;
            background-color: #f4f4f4;
            padding: 1px 3px;
            border-radius: 3px;
        }
        .tech-stack { margin-top: 2pt; font-size: 9.5pt; color: #373737; }
        p { margin-top: 2pt; margin-bottom: 2pt; }
        a { color: #000; text-decoration: none; border-bottom: 0.5pt dotted #000; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Girish Satya Rahul Pinjarla</h1>
        <div class="d-flex justify-content-between align-items-center">
            <div>
                <a href="mailto:rahulpinjarla@gmail.com">rahulpinjarla@gmail.com</a> | (+91) 9550711381 | Bengaluru, India
            </div>
            <div>
                <a href="https://rahul-pinjarla.github.io/" target="_blank">Portfolio: rahul-pinjarla.github.io</a>
            </div>
        </div>
        <hr />

        <h3 class="section-title">Professional Summary</h3>
        <hr />
        <div class="mx-4">
            <p>
                <b>Full-Stack Engineer</b> with 5+ years of experience specializing in high-performance web applications
                using <code>Python (Django, FastAPI)</code> and <code>JavaScript (React, Node)</code>. Proven track
                record in <b>AI/LLM integration</b>, significantly reducing system latency (by 93%), and orchestrating
                scalable microservices on <code>Azure/AWS</code>. Expert in building monetized AI products and
                streamlining complex payment and data workflows.
            </p>
        </div>

        <h3 class="section-title">Skills and Technical Knowledge</h3>
        <hr />
        <div class="mx-4">
            <ul>
                <li><b>Languages:</b> <code>Python, JavaScript, TypeScript, Go, SQL (Postgres)</code>.</li>
                <li><b>Frameworks & Libraries:</b> <code>Django, FastAPI, React.js, Next.js, Node.js, Redux</code>.</li>
                <li><b>Cloud & DevOps:</b> <code>Docker, Kubernetes, Azure, AWS, CI/CD, Linux, Git</code>.</li>
                <li><b>AI & Specialized Tech:</b> <code>LLMs (OpenAI, Gemini), PromptLayer, Vapi.ai, Celery, Redis, RabbitMQ, Convex</code>.</li>
            </ul>
        </div>

        <h3 class="section-title">Work Experience</h3>
        <hr />

        <div class="mx-4">
            <div class="d-flex">
                <h5><b>Full Stack Engineer</b> - Aurelium India Pvt. Ltd.</h5>
                <i><b>August 2023</b> - Present</i>
            </div>

            <div style="margin-left: 8pt; margin-top: 4pt;">
                <div class="d-flex justify-content-between align-items-baseline">
                    <span><b>Product Focus: <a href="https://scouto.com/" target="_blank">Scouto</a></b> (AI Hiring
                        Agency)</span>
                    <small><i>Feb 2025 - Present</i></small>
                </div>
                <i>Key Accomplishments:</i>
                <ul>
                    <li><b>Architected</b> an autonomous voice agent using <b><i>Vapi.ai</i></b> that leverages <b><i>asynchronous processing</i></b> to handle and analyze hundreds of concurrent calls with high reliability.</li>
                    <li>Integrated <b><i>PromptLayer</i></b> to monitor and evaluate prompt performance, empowering stakeholders to manage prompts effortlessly.</li>
                </ul>
                <p class="tech-stack"><b>Tech Stack:</b> <code>TypeScript, Node, NextJS, Convex, PromptLayer, Gemini, ChatGPT, Vapi.ai.</code></p>
            </div>

            <div style="margin-left: 8pt; margin-top: 6pt;">
                <div class="d-flex justify-content-between align-items-baseline">
                    <span><b>Product Focus: <a href="https://pyjamahr.com/" target="_blank">PyjamaHR</a></b> (ATS
                        Platform)</span>
                    <small><i>Aug 2023 - Present</i></small>
                </div>
                <i>Key Accomplishments:</i>
                <ul>
                    <li>Migrated resume parsing from legacy NLP to a <b><i>robust AI agent system</i></b>, achieving a <b><i>98% success rate</i></b> and processing <b><i>50+ resumes in under 2 mins</i></b> via async pipelines.</li>
                    <li>Served as <b>Lead Engineer</b> for the monetized <b><i>AI video interview chatbot</i></b>, driving widespread adoption among international clients.</li>
                    <li><b>Engineered</b> all payment integration flows, successfully integrating <b><i>Stripe</i></b> for seamless transactions.</li>
                    <li>Optimized React build process, reducing initial page load time from <b><i>~7s to ~0.5s (93% improvement)</i></b>.</li>
                    <li>Re-engineered Reports API to handle <b><i>50M+ candidate records</i></b>, delivering analytics in <b><i>under a second</i></b>.</li>
                </ul>
                <p class="tech-stack"><b>Tech Stack:</b> <code>Django, PostgreSQL, Celery, React, NextJS, Redis, Docker, Kubernetes, Azure.</code></p>
            </div>
        </div>

        <div class="mx-4" style="margin-top: 8pt;">
            <div class="d-flex">
                <h5><b>Software Engineer (Full Stack)</b> - Highbreed India Development</h5>
                <i><b>July 2021</b> - Aug 2023</i>
            </div>
            <p><b>Product: - <a href="https://mrkt365.com" target="_blank">Mrkt365</a></b></p>
            <i>Key Accomplishments:</i>
            <ul>
                <li>Developed a real-time messaging application using <code>WebSockets</code> and <code>RabbitMQ</code>, resulting in <b><i>significantly increased user activity</i></b>.</li>
                <li>Engineered a comprehensive Super Admin portal from scratch, making administration level management <b><i>effortless</i></b>.</li>
            </ul>
            <p class="tech-stack"><b>Tech Stack:</b> <code>FastAPI, PostgreSQL, React, Angular, RabbitMQ, Docker, Celery, AWS.</code></p>
        </div>
        <hr />

        <h3 class="section-title">Education</h3>
        <hr />
        <div class="mx-4">
            <div class="d-flex justify-content-between">
                <b><a href="https://rguktsklm.ac.in/" target="_blank">Rajiv Gandhi University of Knowledge Technologies,
                        Srikakulam</a></b>
                <i>2018-2022</i>
            </div>
            <div class="d-flex">
                <p>B.Tech in Computer Science and Engineering</p>
                <i>CGPA: 8.9</i>
            </div>
        </div>

        <h3 class="section-title">Certifications, Languages & Interests</h3>
<hr />
<div class="mx-4">
    <p><b>Certifications:</b> Django Skill Badge (LinkedIn), Python & Problem Solving (HackerRank), DSA (CCBP 4.0), IELTS (7.0)</p>
    <p><b>Languages:</b> English, Hindi, Telugu (Native)</p>
    <p><b>Interests:</b> Coding, Automating tasks, Chess, Foosball, Table Tennis, Music, Anime, Sci-Fi Movies.</p>
</div>
    </div>
</body>
</html>
"""

HTML(string=html_content).write_pdf("Girish_Pinjarla_Resume.pdf")