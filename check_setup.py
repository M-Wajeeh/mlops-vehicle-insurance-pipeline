"""
Quick setup verification script
"""
import os

print("=" * 60)
print("MONGODB SETUP VERIFICATION")
print("=" * 60)

mongo_url = os.getenv("MONGODB_URL")

print("\n1️⃣  MONGODB_URL Environment Variable:")
if mongo_url:
    print(f"   ✅ SET: {mongo_url[:60]}...")
else:
    print("   ❌ NOT SET")
    print("\n   FIX: Run this in PowerShell:")
    print('   $env:MONGODB_URL = "mongodb+srv://user:password@cluster.mongodb.net/?retryWrites=true&w=majority"')

print("\n2️⃣  Sample Data File:")
if os.path.exists("notebook/data.csv"):
    print("   ✅ Found: notebook/data.csv")
else:
    print("   ❌ Missing: notebook/data.csv")

print("\n3️⃣  Next Steps:")
if not mongo_url:
    print("   Step 1: Set MONGODB_URL (see above)")
    print("   Step 2: python load_sample_data.py")
    print("   Step 3: python demo.py")
else:
    print("   ✅ MONGODB_URL is set!")
    print("   Run: python load_sample_data.py")
    print("   Then: python demo.py")

print("\n" + "=" * 60)
