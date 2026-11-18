# Official MCP Registry metadata

These `server.json` files describe the hosted Apify MCP endpoints for three dedicated_crest tools, so they can be published to the [official MCP Registry](https://modelcontextprotocol.io/registry/quickstart) under the `io.github.benbarazandeh/` namespace. Directories that copy the registry (including [Glama](https://glama.ai/mcp/faq)) can then list each tool.

This repo is not a standalone MCP server. The remote URL is Apify's hosted server, scoped to one Actor:

```
https://mcp.apify.com/?tools=dedicated_crest/<actor>
```

On first use, sign in to Apify with OAuth, or pass an Apify API token as `Authorization: Bearer <token>`. Runs are billed to your own Apify account. A new account can start on the Free plan ($5 of monthly platform credit, no credit card).

| Tool | Store page | `server.json` |
|---|---|---|
| Grants.gov Opportunity Finder | [dedicated_crest/grants-gov-opportunity-finder](https://apify.com/dedicated_crest/grants-gov-opportunity-finder) | [`grants-gov-opportunity-finder/server.json`](grants-gov-opportunity-finder/server.json) |
| GDELT News Monitor | [dedicated_crest/gdelt-news-monitor](https://apify.com/dedicated_crest/gdelt-news-monitor) | [`gdelt-news-monitor/server.json`](gdelt-news-monitor/server.json) |
| FMCSA Trucking Carrier Leads | [dedicated_crest/fmcsa-trucking-carrier-leads](https://apify.com/dedicated_crest/fmcsa-trucking-carrier-leads) | [`fmcsa-trucking-carrier-leads/server.json`](fmcsa-trucking-carrier-leads/server.json) |

The generic Apify MCP server is already in the registry as `com.apify/apify-mcp-server`. Do not publish a second generic listing.

## Publish (when ready)

Publishing is a separate step from adding these files. It needs a one-time `mcp-publisher login github` (GitHub device-code sign-in as `benbarazandeh`), then, from each tool directory:

```bash
mcp-publisher validate
mcp-publisher publish
```

After a successful publish, confirm with:

```bash
curl "https://registry.modelcontextprotocol.io/v0.1/servers?search=io.github.benbarazandeh/grants-gov-opportunity-finder"
```

Glama syncs official-registry Streamable HTTP endpoints about once an hour. After a connector page appears, claim it with GitHub (the `io.github.benbarazandeh/...` namespace).
