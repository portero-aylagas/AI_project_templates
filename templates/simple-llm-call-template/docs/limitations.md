# Limitations

- The default fake client is deterministic and does not measure model quality.
- Live provider usage needs credentials, budget awareness, and rate-limit
  handling appropriate to the target provider.
- Prompt changes should be covered by focused tests before they are mixed with
  other code changes.
