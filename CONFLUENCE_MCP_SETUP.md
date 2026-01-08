# Atlassian Rovo MCP Server Setup Guide

## Overview

This guide walks you through setting up the Atlassian Rovo MCP Server to enable Cursor IDE to interact with your Confluence, Jira, and Compass data.

## Prerequisites

✅ **Completed:**
- Node.js v18+ (You have v24.12.0)
- `mcp-remote` package installed globally
- Cursor IDE MCP configuration created

✅ **Required:**
- Atlassian Cloud site access (neoslife.atlassian.net)
- Permissions to access Confluence, Jira, or Compass
- Modern web browser for OAuth authentication

## What Was Configured

### 1. Installed MCP Remote Package

```bash
npm install -g mcp-remote
```

This package acts as a proxy between Cursor and the Atlassian Rovo MCP Server.

### 2. Created Cursor MCP Configuration

**Location:** `~/Library/Application Support/Cursor/User/globalStorage/saoudrizwan.claude-dev/settings/cline_mcp_settings.json`

**Configuration:**
```json
{
  "mcpServers": {
    "atlassian-rovo": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote",
        "https://mcp.atlassian.com/v1/mcp"
      ],
      "env": {}
    }
  }
}
```

## Next Steps: Authentication

### Step 1: Restart Cursor

1. Quit Cursor completely (Cmd+Q)
2. Reopen Cursor
3. Open this project: `/Users/bowen.li/development/repo-wiki-agent-skills`

### Step 2: Trigger OAuth Authentication

When you first use an MCP tool that requires Atlassian access, you'll be prompted to:

1. **Authorize the connection** - A browser window will open
2. **Log in to Atlassian** - Use your neoslife.atlassian.net credentials
3. **Grant permissions** - Approve access to Confluence, Jira, and Compass
4. **Complete OAuth flow** - Return to Cursor

### Step 3: Verify Connection

After authentication, you can test the connection by asking Cursor to:

- "List my Confluence spaces"
- "Search for pages in the Technology space"
- "Show me recent Jira issues"

## Available MCP Tools

Once authenticated, you'll have access to these Atlassian Rovo MCP Server capabilities:

### Confluence Tools
- **Search pages** - Find content across spaces
- **Fetch pages** - Retrieve specific page content
- **Create pages** - Generate new documentation
- **Update pages** - Modify existing content
- **List spaces** - View accessible spaces

### Jira Tools
- **Search issues** - Find tickets by JQL
- **Create issues** - Generate new tickets
- **Update issues** - Modify existing tickets
- **Bulk create** - Create multiple issues at once

### Compass Tools
- **Query components** - Find services and dependencies
- **Create components** - Add new services
- **Bulk import** - Import from CSV/JSON

## Publishing to Confluence

### Target Location

**Space:** Technology  
**Folder:** FDE  
**URL:** https://neoslife.atlassian.net/wiki/spaces/Technology/folder/2083815477

### Publishing Workflow

Once MCP is set up and authenticated, you can:

1. **Create a new page** in the FDE folder
2. **Use MCP tools** to publish content directly from Cursor
3. **Update pages** incrementally as documentation changes

### Example Commands

```
# Create a new page
"Create a Confluence page titled 'Repo Wiki Agent Skills' in the Technology space under the FDE folder"

# Update existing page
"Update the Confluence page with the latest content from README.md"

# Search for pages
"Find all pages in the FDE folder"
```

## Security and Permissions

### Data Access
- All access respects your existing Atlassian permissions
- OAuth 2.1 ensures secure authentication
- Actions are logged in Atlassian audit logs

### Permission Requirements
- You need access to the Technology space
- You need permission to create/edit pages in the FDE folder
- First-time setup may require admin approval (check with your Atlassian admin)

## Troubleshooting

### Issue: "Your site admin must authorize this app"

**Solution:** The first user to set up MCP must have admin permissions. Contact your Atlassian admin to complete the initial OAuth flow.

### Issue: "You don't have permission to connect from this IP address"

**Solution:** Your organization may have IP allowlisting enabled. Contact your admin to add your IP address or VPN range.

### Issue: MCP tools not appearing in Cursor

**Solutions:**
1. Restart Cursor completely (Cmd+Q, then reopen)
2. Check the MCP configuration file exists and is valid JSON
3. Verify `mcp-remote` is installed: `npm list -g mcp-remote`
4. Check Cursor logs: `~/Library/Logs/Cursor/`

### Issue: OAuth flow doesn't complete

**Solutions:**
1. Ensure you're using the correct Atlassian account
2. Check that you have access to at least one Atlassian product (Jira, Confluence, or Compass)
3. Try clearing browser cookies for atlassian.com
4. Use an incognito/private browser window

## Configuration Files

### MCP Settings Location
```
~/Library/Application Support/Cursor/User/globalStorage/saoudrizwan.claude-dev/settings/cline_mcp_settings.json
```

### Backup Configuration

To backup your MCP configuration:

```bash
cp ~/Library/Application\ Support/Cursor/User/globalStorage/saoudrizwan.claude-dev/settings/cline_mcp_settings.json \
   ~/development/repo-wiki-agent-skills/mcp_settings_backup.json
```

### Restore Configuration

To restore from backup:

```bash
cp ~/development/repo-wiki-agent-skills/mcp_settings_backup.json \
   ~/Library/Application\ Support/Cursor/User/globalStorage/saoudrizwan.claude-dev/settings/cline_mcp_settings.json
```

## Advanced Configuration

### Adding Multiple MCP Servers

You can add multiple MCP servers to your configuration:

```json
{
  "mcpServers": {
    "atlassian-rovo": {
      "command": "npx",
      "args": ["-y", "mcp-remote", "https://mcp.atlassian.com/v1/mcp"],
      "env": {}
    },
    "another-server": {
      "command": "node",
      "args": ["/path/to/server.js"],
      "env": {}
    }
  }
}
```

### Environment Variables

If needed, you can add environment variables:

```json
{
  "mcpServers": {
    "atlassian-rovo": {
      "command": "npx",
      "args": ["-y", "mcp-remote", "https://mcp.atlassian.com/v1/mcp"],
      "env": {
        "DEBUG": "mcp:*"
      }
    }
  }
}
```

## Resources

- [Atlassian Rovo MCP Server Documentation](https://support.atlassian.com/atlassian-rovo-mcp-server/docs/getting-started-with-the-atlassian-remote-mcp-server/)
- [MCP Specification](https://modelcontextprotocol.io/)
- [Cursor MCP Documentation](https://docs.cursor.com/advanced/mcp)

## Status

✅ **Setup Complete:**
- [x] Node.js v24.12.0 installed
- [x] `mcp-remote` package installed globally
- [x] Cursor MCP configuration created
- [x] Configuration file saved

⏳ **Pending:**
- [ ] Restart Cursor IDE
- [ ] Complete OAuth authentication flow
- [ ] Verify connection to Atlassian
- [ ] Test Confluence page creation
- [ ] Publish Repo Wiki Agent Skills documentation to FDE folder

## Next Action

**Restart Cursor now** to load the new MCP configuration, then try accessing your Confluence space!
