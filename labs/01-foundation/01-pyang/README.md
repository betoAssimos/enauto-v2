# 01-pyang — YANG model exploration

**Day:** 4 of Week 1
**Scope:** Blueprint 1.1, 1.3, 1.4, 1.5
**Dependencies:** Local only. No network. `pyang` from `requirements.txt`.

## What pyang is (one-liner)

A command-line YANG validator and translator. Given a `.yang` file, it produces:
- **`-f tree`** — the RFC 8340 tree diagram (what the model looks like as a path).
- **`-f sample-json-skeleton`** — a JSON template showing the payload shape.
- **`-f sample-xml-skeleton`** — an XML template showing the same.

These three commands map directly to blueprint sub-topics 1.5, 1.3, 1.4 respectively.

## What we'll do on Day 4

The lab walks one domain — **interfaces** — across three YANG flavors. Same conceptual data, three different module designs. This is the single most efficient way to internalize blueprint 1.1.

**Theory walk first.** Before any `pyang` command runs, we cover:
1. Where YANG models come from (GitHub: `YangModels/yang`, `openconfig/public`, vendor sites).
2. Module namespace conventions (`openconfig-*`, `ietf-*`, `Cisco-IOS-XE-*`).
3. What a YANG `container` vs `list` vs `leaf` looks like in tree form.
4. The RFC 8340 symbol set in detail.

**Then we run.** Piece by piece:
1. Fetch the three modules, save to `yang-models/`, note the source URLs.
2. `pyang -f tree` on each. Read the output together. Identify symbols.
3. `pyang -f sample-json-skeleton` on OpenConfig interfaces. Trace each line back to the tree.
4. `pyang -f sample-xml-skeleton` on the same. Compare namespace placement vs JSON.
5. Note the three structural differences in your notes file.

## Models to acquire (Day 4 task)

We'll pick the actual filenames live, but expect to use modules in this neighborhood:

| Flavor | Source | Module name pattern |
|---|---|---|
| OpenConfig | github.com/openconfig/public | `openconfig-interfaces.yang` |
| IETF | github.com/YangModels/yang (standard/ietf/RFC) | `ietf-interfaces.yang` |
| Cisco native | github.com/YangModels/yang (vendor/cisco/xe) | A `Cisco-IOS-XE-*-interfaces` module from a recent IOS-XE release |

Sources are noted on Day 4 so the lab is reproducible.

## Output layout

```
01-pyang/
├── README.md                              # this file
├── yang-models/                           # populated Day 4
│   ├── openconfig-interfaces.yang
│   ├── ietf-interfaces.yang
│   └── Cisco-IOS-XE-*-interfaces.yang
└── output/                                # created Day 4
    ├── openconfig-tree.txt
    ├── ietf-tree.txt
    ├── cisco-native-tree.txt
    ├── openconfig-interfaces-skeleton.json
    └── openconfig-interfaces-skeleton.xml
```

## Exam payoff

After this lab, the following exam question shapes become trivial:

- "Given this YANG tree, what is the XPath to `<leaf>`?"
- "Which of the following module names is OpenConfig?"
- "What JSON payload corresponds to setting `<leaf>` to `<value>`?"
- "What XML namespace identifies this module?"
