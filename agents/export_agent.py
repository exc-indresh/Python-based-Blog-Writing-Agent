import os
import re
import json
from datetime import datetime

def safe_filename(text):
    """Sanitize the topic to be a safe filename."""
    return re.sub(r'[^\w\-]+', '_', text.lower())

def export_blog(topic, content, meta):
    # Ensure the output directory exists
    os.makedirs("output", exist_ok=True)

    # Timestamped and sanitized filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename_prefix = f"{timestamp}_{safe_filename(topic)}"

    blog_path = f"output/blog_{filename_prefix}.md"
    meta_path = f"output/meta_{filename_prefix}.json"

    # Write content
    with open(blog_path, "w", encoding="utf-8") as f:
        f.write(content)

    # Write meta
    with open(meta_path, "w", encoding="utf-8") as f:
        json.dump(meta, f, indent=2)

    print(f"✅ Blog saved to {blog_path}")
    print(f"✅ Meta saved to {meta_path}")
