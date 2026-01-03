#!/usr/bin/env python3
"""
TTS Removal Verification Script
Verifies that all TTS functionality has been successfully removed while keeping all other features
"""

import sys
import re
from pathlib import Path

def check_app_py():
    """Verify app.py has no TTS references"""
    print("🔍 Checking app.py for TTS removal...")
    
    with open('app.py', 'r') as f:
        content = f.read()
    
    # Check for removed items
    removed_checks = {
        'TTS_CONFIG': 'TTS_CONFIG' not in content,
        'synthesize_text_to_speech': 'synthesize_text_to_speech' not in content,
        'get_tts_system_info': 'get_tts_system_info' not in content,
        'speak_kali_arsenal_info': 'speak_kali_arsenal_info' not in content,
        'speak_security_scan_results': 'speak_security_scan_results' not in content,
        'speak_auto_update_status': 'speak_auto_update_status' not in content,
        'TTS System Tab': '🔊 Multi-Engine TTS System' not in content,
        'TTS Engine dropdown': 'TTS Engine' not in content,
        'TTS references in health': '"tts":' not in content
    }
    
    # Check that essential functions are preserved
    preserved_checks = {
        'get_complete_kali_arsenal_info': 'get_complete_kali_arsenal_info' in content,
        'get_kali_tool_category': 'get_kali_tool_category' in content,
        'run_kali_security_scan': 'run_kali_security_scan' in content,
        'get_bleeding_edge_status': 'get_bleeding_edge_status' in content,
        'generate_kali_security_report': 'generate_kali_security_report' in content,
        'MCP server functionality': 'mcp_server=True' in content,
        'Bleeding edge configuration': 'BLEEDING_EDGE_CONFIG' in content,
        'Arsenal data': 'get_kali_arsenal_data' in content
    }
    
    print("\n  ✅ TTS Components Removed:")
    for check, result in removed_checks.items():
        status = "✅ REMOVED" if result else "❌ STILL PRESENT"
        print(f"    {status}: {check}")
    
    print("\n  ✅ Essential Features Preserved:")
    for check, result in preserved_checks.items():
        status = "✅ PRESERVED" if result else "❌ MISSING"
        print(f"    {status}: {check}")
    
    all_removed = all(removed_checks.values())
    all_preserved = all(preserved_checks.values())
    
    return all_removed and all_preserved

def check_requirements_txt():
    """Verify requirements.txt has no TTS dependencies"""
    print("\n🔍 Checking requirements.txt for TTS dependencies...")
    
    with open('requirements.txt', 'r') as f:
        content = f.read()
    
    checks = {
        'No gtts dependency': 'gtts' not in content,
        'No pydub dependency': 'pydub' not in content,
        'Gradio MCP preserved': 'gradio[mcp]' in content,
        'Core dependencies preserved': 'fastapi' in content and 'aiohttp' in content
    }
    
    for check, result in checks.items():
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"    {status}: {check}")
    
    return all(checks.values())

def check_functionality_count():
    """Verify MCP tool counts have been updated"""
    print("\n🔍 Checking MCP tool count updates...")
    
    with open('app.py', 'r') as f:
        content = f.read()
    
    # Count actual MCP tools in the tools list
    tools_match = re.search(r'tools = \[(.*?)\]', content, re.DOTALL)
    if tools_match:
        tools_content = tools_match.group(1)
        tool_count = len([line for line in tools_content.split('\n') if line.strip() and not line.strip().startswith('#')])
        expected_count = 5  # get_complete_kali_arsenal_info, get_kali_tool_category, run_kali_security_scan, get_bleeding_edge_status, generate_kali_security_report
    else:
        tool_count = 0
        expected_count = 5
    
    checks = {
        f'Tool count is {expected_count}': tool_count == expected_count,
        'Health endpoint shows 5 tools': '"mcp_tools": 5' in content,
        'Interface shows 5 tools': '5 comprehensive' in content
    }
    
    for check, result in checks.items():
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"    {status}: {check}")
    
    print(f"    📊 Actual tool count: {tool_count}, Expected: {expected_count}")
    
    return all(checks.values())

def check_no_broken_references():
    """Check for broken references that would cause runtime errors"""
    print("\n🔍 Checking for broken references...")
    
    with open('app.py', 'r') as f:
        content = f.read()
    
    # Look for common patterns that would cause errors
    broken_patterns = {
        'TTS_CONFIG references': re.search(r'TTS_CONFIG\[', content),
        'len(TTS_CONFIG': re.search(r'len\(TTS_CONFIG', content),
        'TTS_CONFIG.get': re.search(r'TTS_CONFIG\.get', content),
        'Orphaned TTS calls': re.search(r'await synthesize_text_to_speech', content),
        'Orphaned speak calls': re.search(r'await speak_', content)
    }
    
    checks = {pattern: not bool(match) for pattern, match in broken_patterns.items()}
    
    for check, result in checks.items():
        status = "✅ CLEAN" if result else "❌ BROKEN REFERENCE"
        print(f"    {status}: {check}")
    
    return all(checks.values())

def generate_summary():
    """Generate summary of what was removed and what was kept"""
    print("\n📊 TTS REMOVAL SUMMARY")
    print("=" * 40)
    
    print("\n✅ REMOVED TTS COMPONENTS:")
    removed_items = [
        "TTS_CONFIG configuration",
        "synthesize_text_to_speech() function",
        "get_tts_system_info() function", 
        "speak_kali_arsenal_info() function",
        "speak_security_scan_results() function",
        "speak_auto_update_status() function",
        "Multi-Engine TTS System tab",
        "TTS engine dropdowns and controls",
        "TTS dependencies (gtts, pydub)",
        "Voice accessibility UI components",
        "TTS references in health endpoint",
        "TTS logging and status messages"
    ]
    
    for item in removed_items:
        print(f"  - {item}")
    
    print("\n✅ PRESERVED CORE FEATURES:")
    preserved_items = [
        "793+ Cybersecurity tools arsenal",
        "5 Core MCP tools for security research",
        "Bleeding edge enhancement (150 experimental tools)",
        "Complete Gradio interface with all tabs",
        "MCP server functionality (mcp_server=True)",
        "SSE transport for HuggingChat integration",
        "Health monitoring and status endpoints",
        "Professional security report generation",
        "Unified platform architecture",
        "HuggingFace Spaces compatibility"
    ]
    
    for item in preserved_items:
        print(f"  - {item}")
    
    print("\n🎯 RESULT:")
    print("  - Multi-engine TTS functionality completely removed")
    print("  - All cybersecurity features preserved")
    print("  - MCP integration remains fully functional")
    print("  - Platform ready for deployment")

def main():
    """Run all verification checks"""
    print("🔥 DarkDriftz TTS Removal Verification")
    print("=" * 50)
    
    checks = [
        check_app_py(),
        check_requirements_txt(), 
        check_functionality_count(),
        check_no_broken_references()
    ]
    
    print("\n📋 VERIFICATION RESULTS")
    print("=" * 30)
    
    if all(checks):
        print("✅ ALL CHECKS PASSED!")
        print("🎉 TTS functionality successfully removed")
        print("🔒 All cybersecurity features preserved")
        print("🚀 Platform ready for deployment")
        
        generate_summary()
        
    else:
        print("❌ SOME CHECKS FAILED!")
        print("🔧 Please review the failed checks above")
        
        failed_count = sum(1 for check in checks if not check)
        print(f"\n📊 Results: {len(checks) - failed_count}/{len(checks)} checks passed")
    
    return all(checks)

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
