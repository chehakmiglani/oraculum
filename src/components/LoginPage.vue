<script setup lang="ts">
import { ref } from 'vue';
import { useRouter } from 'vue-router';
const router = useRouter();
function startCoaching() {
	router.push('/dashboard');
}
</script>

<template>
	<div class="landing-wrapper">
		<header class="landing-header">
			<img src="../assets/logo.svg" alt="AI Career" class="logo" />
			<span class="brand">AI CAREER</span>
			<button class="community-btn">🚀 Join Our AI Career Community</button>
		</header>
		<main class="landing-main">
			<h1>
				Land Your Dream Job<br />
				with the <span class="highlight">AI Career Coach</span>
			</h1>
			<p class="subtitle">
				Personalized job search, resume tips, mock interviews, and AI guidance for every career level.
			</p>
			<button class="cta" @click="startCoaching">Start Coaching</button>
			<div class="tool-cards-row">
				<div class="tool-card" v-for="tool in tools" :key="tool.title">
					<div class="icon">{{ tool.icon }}</div>
					<div class="title">{{ tool.title }}</div>
					<div class="desc">{{ tool.desc }}</div>
				</div>
			</div>
		</main>
	</div>
</template>

<script lang="ts">
export default {
	data() {
		return {
			tools: [
				{ icon: '🗨️', title: 'AI Career Chat Q&A', desc: 'Ask career questions' },
				{ icon: '📄', title: 'AI Resume Analyzer', desc: 'Improve your resume' },
				{ icon: '🛣️', title: 'AI Roadmap Generator', desc: 'Build your roadmap' },
				{ icon: '✉️', title: 'AI Cover Letter Generator', desc: 'Write a cover letter' },
			],
		};
	},
};
</script>

<style scoped>
.landing-wrapper {
	min-height: 100vh;
	background: #f8fafc;
	display: flex;
	flex-direction: column;
	align-items: center;
}
.landing-header {
	display: flex;
	align-items: center;
	gap: 1rem;
	padding: 2rem 0 1rem 0;
}
.logo {
	width: 40px;
	height: 40px;
}
.brand {
	font-weight: bold;
	font-size: 1.5rem;
	color: #3b82f6;
}
.community-btn {
	background: #f3f4f6;
	color: #374151;
	border-radius: 999px;
	padding: 0.5rem 1.5rem;
	font-size: 1rem;
	margin-left: 2rem;
	border: none;
	cursor: pointer;
}
.landing-main {
	text-align: center;
	margin-top: 2rem;
}
h1 {
	font-size: 2.5rem;
	font-weight: bold;
	margin-bottom: 1rem;
}
.highlight {
	color: #3b82f6;
}
.subtitle {
	color: #6b7280;
	font-size: 1.2rem;
	margin-bottom: 2rem;
}
.cta {
	background: linear-gradient(90deg, #6366f1, #3b82f6);
	color: #fff;
	border: none;
	border-radius: 8px;
	padding: 0.75rem 2rem;
	font-size: 1.1rem;
	cursor: pointer;
	box-shadow: 0 2px 8px rgba(59,130,246,0.08);
	transition: background 0.2s;
	margin-bottom: 2rem;
}
.cta:hover {
	background: linear-gradient(90deg, #3b82f6, #6366f1);
}
.tool-cards-row {
	display: flex;
	justify-content: center;
	gap: 2rem;
	margin: 2rem 0;
	flex-wrap: wrap;
}
.tool-card {
	background: #fff;
	border-radius: 12px;
	box-shadow: 0 2px 8px rgba(0,0,0,0.06);
	padding: 2rem 1.5rem;
	width: 220px;
	text-align: center;
	display: flex;
	flex-direction: column;
	align-items: center;
}
.icon {
	font-size: 2.2rem;
	margin-bottom: 1rem;
}
.title {
	font-weight: bold;
	font-size: 1.1rem;
	margin-bottom: 0.5rem;
}
.desc {
	color: #6b7280;
	font-size: 0.95rem;
	margin-bottom: 1.2rem;
}
</style>
