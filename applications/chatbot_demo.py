#!/usr/bin/env python3
"""
MojoMosaic Intelligent Chatbot
Roman Urdu mein bhi kaam karta hai!
"""

import asyncio
import json
from datetime import datetime
from typing import Dict, List, Any
import random

class MojoMosaicChatbot:
    def __init__(self):
        self.context_memory = {}
        self.user_preferences = {}
        self.conversation_history = []
        
    async def process_message(self, user_input: str, user_id: str = "default") -> str:
        """Process user message through fractal intelligence layers"""
        
        # Dimension 1-3: Basic Understanding
        intent = await self._analyze_intent(user_input)
        language = await self._detect_language(user_input)
        sentiment = await self._analyze_sentiment(user_input)
        
        # Dimension 4-6: Context Building  
        context = await self._build_context(user_input, user_id)
        
        # Dimension 7-9: Response Generation
        response = await self._generate_response(user_input, intent, language, context)
        
        # Store conversation
        self.conversation_history.append({
            "timestamp": datetime.now().isoformat(),
            "user": user_input,
            "bot": response,
            "intent": intent,
            "language": language,
            "sentiment": sentiment
        })
        
        return response
    
    async def _analyze_intent(self, text: str) -> str:
        """Analyze user intent"""
        greetings = ["hello", "hi", "salam", "assalam", "namaste", "adaab"]
        questions = ["kya", "what", "how", "kaise", "kahan", "where", "kon", "who"]
        requests = ["help", "madad", "please", "karo", "batao", "dikhao"]
        
        text_lower = text.lower()
        
        if any(word in text_lower for word in greetings):
            return "greeting"
        elif any(word in text_lower for word in questions):
            return "question"
        elif any(word in text_lower for word in requests):
            return "request"
        else:
            return "general"
    
    async def _detect_language(self, text: str) -> str:
        """Detect language (English/Roman Urdu)"""
        urdu_words = ["hai", "ka", "ke", "ki", "kya", "kaise", "kahan", "abi", "bhi", 
                      "meri", "tera", "tumhara", "samajh", "batao", "karo", "dekho"]
        
        if any(word in text.lower() for word in urdu_words):
            return "roman_urdu"
        return "english"
    
    async def _analyze_sentiment(self, text: str) -> str:
        """Simple sentiment analysis"""
        positive_words = ["good", "great", "amazing", "awesome", "theek", "acha", "zabardast"]
        negative_words = ["bad", "terrible", "awful", "bura", "ganda", "kharab"]
        
        text_lower = text.lower()
        
        if any(word in text_lower for word in positive_words):
            return "positive"
        elif any(word in text_lower for word in negative_words):
            return "negative"
        return "neutral"
    
    async def _build_context(self, text: str, user_id: str) -> Dict:
        """Build conversation context"""
        if user_id not in self.context_memory:
            self.context_memory[user_id] = {
                "conversation_count": 0,
                "topics": [],
                "preferences": {}
            }
        
        self.context_memory[user_id]["conversation_count"] += 1
        return self.context_memory[user_id]
    
    async def _generate_response(self, text: str, intent: str, language: str, context: Dict) -> str:
        """Generate intelligent response"""
        
        if language == "roman_urdu":
            return await self._generate_urdu_response(text, intent, context)
        else:
            return await self._generate_english_response(text, intent, context)
    
    async def _generate_urdu_response(self, text: str, intent: str, context: Dict) -> str:
        """Generate Roman Urdu responses"""
        responses = {
            "greeting": [
                "Assalam alaikum! Kaise hain aap?",
                "Salam bhai! Kya haal hai?",
                "Hello! Main aapki kaise madad kar sakta hun?",
                "Namaste! Batao kya chahiye?"
            ],
            "question": [
                "Acha sawal hai! Main samjhane ki koshish karta hun...",
                "Bilkul puch sakte hain, main batata hun...",
                "Ye interesting topic hai, dekho...",
                "Main detail mein explain karta hun..."
            ],
            "request": [
                "Bilkul! Main aapki madad karta hun.",
                "Zaroor, batao kya karna hai.",
                "Sure thing! Kaise help kar sakta hun?",
                "Theek hai, main kar deta hun ye kaam."
            ],
            "general": [
                "Samajh gaya. Aur kuch puchna hai?",
                "Theek hai. Koi aur query?",
                "OK. Batao aur kya discussion karte hain?",
                "Right. Kuch aur topic hai discuss karne ko?"
            ]
        }
        
        # Add context-aware responses
        count = context.get("conversation_count", 1)
        if count > 5:
            responses[intent].append("Waise hum bahut baat kar chuke hain! 😄")
        
        return random.choice(responses.get(intent, responses["general"]))
    
    async def _generate_english_response(self, text: str, intent: str, context: Dict) -> str:
        """Generate English responses"""
        responses = {
            "greeting": [
                "Hello! How can I help you today?",
                "Hi there! What can I do for you?",
                "Greetings! How may I assist you?",
                "Hey! What's on your mind?"
            ],
            "question": [
                "That's a great question! Let me explain...",
                "Interesting query! Here's what I think...",
                "Good point! Let me break it down...",
                "Nice question! Here's my take..."
            ],
            "request": [
                "Absolutely! I'll help you with that.",
                "Sure thing! What do you need?",
                "Of course! How can I assist?",
                "I'd be happy to help!"
            ],
            "general": [
                "I understand. Anything else?",
                "Got it. What else can we discuss?",
                "Noted. Any other questions?",
                "Understood. What's next?"
            ]
        }
        
        return random.choice(responses.get(intent, responses["general"]))

async def demo_chatbot():
    """Demo the chatbot functionality"""
    bot = MojoMosaicChatbot()
    
    print("🤖 MojoMosaic Chatbot Demo")
    print("=" * 40)
    print("Both English and Roman Urdu supported!")
    print("Type 'quit' to exit")
    print("=" * 40)
    
    test_messages = [
        "Hello there!",
        "Salam bhai, kya haal hai?",
        "Chatbot kaise banate hain?",
        "Mujhe madad chahiye",
        "This is amazing!",
        "Ye system kitna zabardast hai!",
        "quit"
    ]
    
    for message in test_messages:
        if message.lower() == 'quit':
            break
            
        print(f"\n👤 User: {message}")
        response = await bot.process_message(message)
        print(f"🤖 Bot: {response}")
        
        # Small delay for demo effect
        await asyncio.sleep(0.5)
    
    print("\n📊 Conversation History:")
    for i, conv in enumerate(bot.conversation_history[-3:], 1):
        print(f"{i}. [{conv['language']}] {conv['intent']} - {conv['sentiment']}")

if __name__ == "__main__":
    asyncio.run(demo_chatbot()) 