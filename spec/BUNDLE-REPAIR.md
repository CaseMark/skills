# Recovering older published bundles

Git remains the authoring source. `content.skills` and `content.skill_source_files`
remain the published catalog; this does not copy content into `public.skills` or
change the website/catalog-dispatch pipeline.

`Repair Published Bundles` is manual and **read-only by default**. With no slugs,
it inventories tracked legal bundles containing companion files against exact
source bytes, sizes, encoding, and live MCP companion rows. Domain timestamps
alone cannot establish bundle completeness.

For a repair, review the inventory and use an explicit list of at most 20 slugs,
`apply=true`, and the exact reviewed **main commit SHA** in `approved_sha`.
No full-catalog apply is supported. An empty list, unreviewed SHA, retired slug,
missing/archived root, changed root metadata/content, or missing embedding blocks
the repair. All selected roots are validated before any writes.

The command reuses the normal publisher's per-bundle transaction with the existing
embedding. It locks and checks the root's version before updating the root version,
source manifest, and MCP files together. Removed companions are archived. A failed
file insert or concurrent root update rolls the whole bundle back. The batch is
not one cross-bundle transaction: completed bundles remain published if a later
bundle fails. Rerun the dry-run inventory before retrying.

Author attribution, aliases/original snapshots, tenant skills, permissions, prices,
and installations are untouched. Publishing a script is not execution approval.
This workflow does not enable MCP for any additional organization.

## CD-1869 initial repair

The isolated verification target is `medical-records-gap-analysis`: its root is
already current, but four tracked `references/*.md` files were not published by
the historical root-only publisher. Review and repair that slug first after this
tooling is merged. Other inventory findings require their own explicit reviewed
selection; do not substitute `full_sync=true`.

After applying, verify the four reference paths via the website source route,
Case.dev MCP `skills/get`/`resources/read` hashes, and the esq-c3 bundle detail.
P3 reads root instructions through its canonical library adapter; its Marketplace
curation and Provider access are separate from public-source availability.
