#!/usr/bin/env python3
"""
MojoMosaic Intelligent Security System
Real-time monitoring aur threat detection
"""

import asyncio
import json
import time
import random
from datetime import datetime, timedelta
from typing import Dict, List, Any
from dataclasses import dataclass
from enum import Enum

class ThreatLevel(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

@dataclass
class SecurityEvent:
    timestamp: datetime
    event_type: str
    source_ip: str
    threat_level: ThreatLevel
    description: str
    confidence: float
    action_taken: str

class MojoMosaicSecurity:
    def __init__(self):
        self.active_monitoring = True
        self.event_history = []
        self.blocked_ips = set()
        self.threat_patterns = self._load_threat_patterns()
        self.alert_thresholds = {
            ThreatLevel.LOW: 0.3,
            ThreatLevel.MEDIUM: 0.6,
            ThreatLevel.HIGH: 0.8,
            ThreatLevel.CRITICAL: 0.9
        }
    
    def _load_threat_patterns(self) -> Dict:
        """Load known threat patterns"""
        return {
            "sql_injection": [
                "SELECT * FROM", "DROP TABLE", "UNION SELECT", 
                "' OR '1'='1", "admin'--", "1=1"
            ],
            "xss_attack": [
                "<script>", "javascript:", "onerror=", 
                "onload=", "eval(", "document.cookie"
            ],
            "brute_force": [
                "multiple_failed_logins", "password_spray",
                "credential_stuffing", "dictionary_attack"
            ],
            "ddos": [
                "high_request_rate", "bandwidth_spike",
                "connection_flood", "syn_flood"
            ],
            "malware": [
                "suspicious_executable", "encrypted_payload",
                "callback_domain", "persistence_mechanism"
            ]
        }
    
    async def start_monitoring(self):
        """Start real-time security monitoring"""
        print("🛡️  MojoMosaic Security System ACTIVATED")
        print("=" * 50)
        print("Real-time threat detection chalaya ja raha hai...")
        print("=" * 50)
        
        # Simulate multiple monitoring tasks
        tasks = [
            self._monitor_network_traffic(),
            self._monitor_login_attempts(),
            self._monitor_file_system(),
            self._monitor_database_access(),
            self._generate_threat_intelligence()
        ]
        
        await asyncio.gather(*tasks)
    
    async def _monitor_network_traffic(self):
        """Monitor network traffic for anomalies"""
        while self.active_monitoring:
            # Simulate network analysis
            source_ip = f"192.168.1.{random.randint(1, 254)}"
            
            # Random threat simulation
            if random.random() < 0.3:  # 30% chance of suspicious activity
                await self._analyze_suspicious_traffic(source_ip)
            
            await asyncio.sleep(2)
    
    async def _monitor_login_attempts(self):
        """Monitor login attempts"""
        failed_attempts = {}
        
        while self.active_monitoring:
            # Simulate login monitoring
            ip = f"10.0.0.{random.randint(1, 100)}"
            
            if random.random() < 0.2:  # 20% chance of failed login
                failed_attempts[ip] = failed_attempts.get(ip, 0) + 1
                
                if failed_attempts[ip] >= 5:  # Brute force detection
                    await self._handle_brute_force(ip, failed_attempts[ip])
                    failed_attempts[ip] = 0  # Reset counter
            
            await asyncio.sleep(3)
    
    async def _monitor_file_system(self):
        """Monitor file system for unauthorized changes"""
        while self.active_monitoring:
            # Simulate file monitoring
            if random.random() < 0.15:  # 15% chance of file activity
                await self._analyze_file_changes()
            
            await asyncio.sleep(4)
    
    async def _monitor_database_access(self):
        """Monitor database access patterns"""
        while self.active_monitoring:
            # Simulate database monitoring
            if random.random() < 0.1:  # 10% chance of suspicious query
                await self._analyze_database_query()
            
            await asyncio.sleep(5)
    
    async def _generate_threat_intelligence(self):
        """Generate threat intelligence reports"""
        while self.active_monitoring:
            await asyncio.sleep(10)  # Generate report every 10 seconds
            
            recent_events = [e for e in self.event_history 
                           if e.timestamp > datetime.now() - timedelta(minutes=1)]
            
            if recent_events:
                await self._generate_threat_report(recent_events)
    
    async def _analyze_suspicious_traffic(self, source_ip: str):
        """Analyze suspicious network traffic"""
        threat_types = ["ddos", "port_scan", "data_exfiltration", "malware_c2"]
        threat_type = random.choice(threat_types)
        
        confidence = random.uniform(0.4, 0.95)
        threat_level = self._calculate_threat_level(confidence)
        
        event = SecurityEvent(
            timestamp=datetime.now(),
            event_type=f"suspicious_traffic_{threat_type}",
            source_ip=source_ip,
            threat_level=threat_level,
            description=f"Suspicious {threat_type} activity detected from {source_ip}",
            confidence=confidence,
            action_taken=await self._take_security_action(threat_level, source_ip)
        )
        
        self.event_history.append(event)
        await self._log_security_event(event)
    
    async def _handle_brute_force(self, ip: str, attempts: int):
        """Handle brute force attack"""
        event = SecurityEvent(
            timestamp=datetime.now(),
            event_type="brute_force_attack",
            source_ip=ip,
            threat_level=ThreatLevel.HIGH,
            description=f"Brute force attack: {attempts} failed login attempts from {ip}",
            confidence=0.9,
            action_taken=f"IP {ip} blocked for 1 hour"
        )
        
        self.blocked_ips.add(ip)
        self.event_history.append(event)
        await self._log_security_event(event)
    
    async def _analyze_file_changes(self):
        """Analyze unauthorized file changes"""
        files = ["system.conf", "passwd", "authorized_keys", "crontab"]
        file_name = random.choice(files)
        
        confidence = random.uniform(0.5, 0.8)
        threat_level = self._calculate_threat_level(confidence)
        
        event = SecurityEvent(
            timestamp=datetime.now(),
            event_type="unauthorized_file_change",
            source_ip="localhost",
            threat_level=threat_level,
            description=f"Unauthorized modification detected in {file_name}",
            confidence=confidence,
            action_taken="File change logged and admin notified"
        )
        
        self.event_history.append(event)
        await self._log_security_event(event)
    
    async def _analyze_database_query(self):
        """Analyze suspicious database queries"""
        query_types = ["sql_injection", "data_dump", "privilege_escalation"]
        query_type = random.choice(query_types)
        source_ip = f"172.16.0.{random.randint(1, 50)}"
        
        confidence = random.uniform(0.6, 0.9)
        threat_level = self._calculate_threat_level(confidence)
        
        event = SecurityEvent(
            timestamp=datetime.now(),
            event_type=f"suspicious_db_query_{query_type}",
            source_ip=source_ip,
            threat_level=threat_level,
            description=f"Potential {query_type} attempt detected from {source_ip}",
            confidence=confidence,
            action_taken="Query blocked and connection terminated"
        )
        
        self.event_history.append(event)
        await self._log_security_event(event)
    
    def _calculate_threat_level(self, confidence: float) -> ThreatLevel:
        """Calculate threat level based on confidence"""
        if confidence >= 0.9:
            return ThreatLevel.CRITICAL
        elif confidence >= 0.8:
            return ThreatLevel.HIGH
        elif confidence >= 0.6:
            return ThreatLevel.MEDIUM
        else:
            return ThreatLevel.LOW
    
    async def _take_security_action(self, threat_level: ThreatLevel, source_ip: str) -> str:
        """Take appropriate security action"""
        actions = {
            ThreatLevel.LOW: f"Logged for monitoring",
            ThreatLevel.MEDIUM: f"Rate limiting applied to {source_ip}",
            ThreatLevel.HIGH: f"IP {source_ip} temporarily blocked",
            ThreatLevel.CRITICAL: f"IP {source_ip} permanently blocked, admin alerted"
        }
        
        if threat_level in [ThreatLevel.HIGH, ThreatLevel.CRITICAL]:
            self.blocked_ips.add(source_ip)
        
        return actions.get(threat_level, "No action taken")
    
    async def _log_security_event(self, event: SecurityEvent):
        """Log security event"""
        emoji_map = {
            ThreatLevel.LOW: "🟡",
            ThreatLevel.MEDIUM: "🟠", 
            ThreatLevel.HIGH: "🔴",
            ThreatLevel.CRITICAL: "🚨"
        }
        
        emoji = emoji_map.get(event.threat_level, "ℹ️")
        
        print(f"\n{emoji} [{event.timestamp.strftime('%H:%M:%S')}] "
              f"{event.threat_level.value.upper()} - {event.event_type}")
        print(f"   📍 Source: {event.source_ip}")
        print(f"   📝 {event.description}")
        print(f"   🎯 Confidence: {event.confidence:.2%}")
        print(f"   ⚡ Action: {event.action_taken}")
    
    async def _generate_threat_report(self, events: List[SecurityEvent]):
        """Generate threat intelligence report"""
        if not events:
            return
        
        threat_counts = {}
        for event in events:
            threat_counts[event.threat_level] = threat_counts.get(event.threat_level, 0) + 1
        
        print(f"\n📊 THREAT INTELLIGENCE REPORT - {datetime.now().strftime('%H:%M:%S')}")
        print("=" * 40)
        for level, count in threat_counts.items():
            print(f"   {level.value.upper()}: {count} events")
        print(f"   Total Blocked IPs: {len(self.blocked_ips)}")
        print("=" * 40)
    
    async def stop_monitoring(self):
        """Stop security monitoring"""
        self.active_monitoring = False
        print("\n🛑 Security monitoring stopped")

async def demo_security_system():
    """Demo the security system"""
    security = MojoMosaicSecurity()
    
    # Run for 30 seconds demo
    try:
        monitoring_task = asyncio.create_task(security.start_monitoring())
        await asyncio.sleep(30)  # Run for 30 seconds
        await security.stop_monitoring()
        monitoring_task.cancel()
        
        # Final report
        print(f"\n📈 FINAL SECURITY SUMMARY")
        print("=" * 40)
        print(f"Total Events Detected: {len(security.event_history)}")
        print(f"IPs Blocked: {len(security.blocked_ips)}")
        
        if security.blocked_ips:
            print("Blocked IPs:", ", ".join(list(security.blocked_ips)[:5]))
        
        # Show recent critical events
        critical_events = [e for e in security.event_history 
                         if e.threat_level == ThreatLevel.CRITICAL]
        print(f"Critical Threats: {len(critical_events)}")
        
    except KeyboardInterrupt:
        await security.stop_monitoring()
        print("\n👋 Security demo terminated by user")

if __name__ == "__main__":
    asyncio.run(demo_security_system()) 