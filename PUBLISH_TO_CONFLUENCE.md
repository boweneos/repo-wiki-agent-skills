# Publishing Repo Wiki Agent Skills to Confluence

## Current Status

✅ MCP configuration is set up  
⏳ Waiting for Cursor restart to activate Atlassian Rovo MCP  
📝 Content is ready in `CONFLUENCE_PAGE_CONTENT.md`

---

## Option 1: Automated Publishing (After Cursor Restart)

### Step 1: Restart Cursor
1. Quit Cursor: `Cmd + Q`
2. Wait 5 seconds
3. Reopen Cursor
4. Open this project

### Step 2: Authenticate with Atlassian
When prompted:
1. Log in to neoslife.atlassian.net
2. Grant permissions to Confluence
3. Complete OAuth flow

### Step 3: Use MCP to Publish
Once authenticated, run this command in Cursor chat:

```
Create a new Confluence page with the following details:
- Title: "Repo Wiki Agent Skills"
- Space: Technology
- Parent: FDE folder (ID: 2083815477)
- Content: Use the content from CONFLUENCE_PAGE_CONTENT.md file

Make sure to format it properly with:
- Proper headings
- Code blocks
- Tables
- Links
```

---

## Option 2: Manual Publishing (Available Now)

### Step 1: Log in to Confluence
1. Open browser: https://neoslife.atlassian.net/wiki/spaces/Technology/folder/2083815477
2. Log in with your credentials

### Step 2: Create New Page
1. Click **Create** button (or press `C`)
2. Select **Blank page**
3. Set parent location to **FDE folder**

### Step 3: Copy Content
1. Open `CONFLUENCE_PAGE_CONTENT.md` in this project
2. Copy all content (Cmd+A, Cmd+C)
3. Paste into Confluence editor

### Step 4: Format the Page

Confluence will auto-format most Markdown, but you may need to:

**Fix Code Blocks:**
- Select code blocks
- Click the `{}` button to format as code
- Set language (bash, json, markdown, etc.)

**Fix Tables:**
- Tables should auto-format
- Adjust column widths if needed

**Fix Links:**
- Update any relative links to absolute URLs
- Ensure GitHub links work: https://github.com/boweneos/repo-wiki-agent-skills

**Add Info Panels (Optional):**
- Select key sections
- Use `{` macro button
- Choose "Info" or "Note" panel

### Step 5: Set Page Properties
1. **Title:** Repo Wiki Agent Skills
2. **Parent:** FDE folder
3. **Labels:** Add relevant labels (e.g., `documentation`, `agent-skills`, `ai`, `wiki`)

### Step 6: Publish
1. Review the page
2. Click **Publish** button
3. Share the link with your team

---

## Option 3: Import Markdown (Confluence Cloud)

### Step 1: Prepare Markdown File
The file is already prepared: `CONFLUENCE_PAGE_CONTENT.md`

### Step 2: Navigate to FDE Folder
https://neoslife.atlassian.net/wiki/spaces/Technology/folder/2083815477

### Step 3: Import Markdown
1. Click **Create** → **Import**
2. Select **Markdown**
3. Upload `CONFLUENCE_PAGE_CONTENT.md`
4. Review the preview
5. Click **Import**

### Step 4: Adjust Formatting
Confluence may need some adjustments:
- Check code block formatting
- Verify table rendering
- Fix any broken links
- Add labels

---

## Quick Copy-Paste Guide

### For Confluence Editor

1. **Open Confluence page editor**
2. **Copy this content** from `CONFLUENCE_PAGE_CONTENT.md`
3. **Paste into editor**
4. **Adjust formatting:**

#### Headers
- Confluence will auto-convert `#` to H1, `##` to H2, etc.

#### Code Blocks
- Wrap in triple backticks with language:
  ```bash
  ./scripts/wiki-init.sh
  ```

#### Tables
- Confluence auto-formats Markdown tables
- Example:
  ```markdown
  | Column 1 | Column 2 |
  |----------|----------|
  | Value 1  | Value 2  |
  ```

#### Links
- Markdown links work: `[text](url)`
- Example: `[GitHub](https://github.com/boweneos/repo-wiki-agent-skills)`

#### Emojis
- Confluence supports emojis: 🚀 ✅ 📋 🔧

---

## After Publishing

### Share the Page
1. Get the page URL
2. Share with your team
3. Add to relevant documentation indexes

### Set Permissions (If Needed)
1. Click **•••** (More actions)
2. Select **Restrictions**
3. Configure who can view/edit

### Add to Navigation
1. Consider adding to space sidebar
2. Link from other relevant pages
3. Add to team onboarding docs

---

## Verification Checklist

After publishing, verify:

- [ ] Page title is "Repo Wiki Agent Skills"
- [ ] Page is in the FDE folder
- [ ] All headings are properly formatted
- [ ] Code blocks are syntax-highlighted
- [ ] Tables render correctly
- [ ] Links work (especially GitHub links)
- [ ] Images/diagrams display (if any)
- [ ] Page is accessible to team members
- [ ] Labels are added

---

## Troubleshooting

### Content Doesn't Format Properly
- Try using Confluence's Markdown import feature
- Or manually format sections using Confluence's editor tools

### Can't Find FDE Folder
- Navigate to Technology space first
- Look in the page tree on the left
- Or use the direct URL: https://neoslife.atlassian.net/wiki/spaces/Technology/folder/2083815477

### Permission Issues
- Contact your Confluence space admin
- You need "Can create" permission in the Technology space

### MCP Not Working After Restart
- Check MCP configuration: `cat ~/Library/Application\ Support/Cursor/User/globalStorage/saoudrizwan.claude-dev/settings/cline_mcp_settings.json`
- Verify `mcp-remote` is installed: `npm list -g mcp-remote`
- Check Cursor logs: `~/Library/Logs/Cursor/`

---

## Alternative: Use Confluence REST API

If you prefer automation without MCP:

```bash
# Set variables
CONFLUENCE_URL="https://neoslife.atlassian.net"
SPACE_KEY="Technology"
PARENT_ID="2083815477"
TITLE="Repo Wiki Agent Skills"

# You'll need an API token from:
# https://id.atlassian.com/manage-profile/security/api-tokens

# Create page (requires curl and jq)
curl -X POST \
  -H "Content-Type: application/json" \
  -u "your-email@example.com:YOUR_API_TOKEN" \
  -d @confluence_payload.json \
  "$CONFLUENCE_URL/wiki/rest/api/content"
```

---

## Summary

**Recommended Approach:**
1. **Restart Cursor** to activate Atlassian Rovo MCP
2. **Authenticate** with Atlassian
3. **Use MCP** to publish automatically

**Quick Alternative:**
1. **Log in** to Confluence
2. **Create page** in FDE folder
3. **Copy-paste** from `CONFLUENCE_PAGE_CONTENT.md`
4. **Adjust formatting** as needed
5. **Publish**

Both methods will get your documentation published to the FDE folder in the Technology space!
