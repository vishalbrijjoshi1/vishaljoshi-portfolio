{\rtf1\ansi\deff0\adeflang1025
{\fonttbl{\f0\froman\fprq2\fcharset0 Times New Roman;}{\f1\froman\fprq2\fcharset2 Symbol;}{\f2\fswiss\fprq2\fcharset0 Arial;}{\f3\fnil\fprq2\fcharset0 Microsoft YaHei;}{\f4\fnil\fprq2\fcharset0 Arial;}{\f5\fswiss\fprq0\fcharset128 Arial;}}
{\colortbl;\red0\green0\blue0;\red128\green128\blue128;}
{\stylesheet{\s0\snext0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393 Default;}
{\s15\sbasedon0\snext16\sb240\sa120\keepn\hich\af3\dbch\af4\afs28\loch\f2\fs28 Heading;}
{\s16\sbasedon0\snext16\sb0\sa120 Text body;}
{\s17\sbasedon16\snext17\sb0\sa120\dbch\af5 List;}
{\s18\sbasedon0\snext18\sb120\sa120\noline\i\dbch\af5\afs24\ai\fs24 Caption;}
{\s19\sbasedon0\snext19\noline\dbch\af5 Index;}
}{\info{\creatim\yr0\mo0\dy0\hr0\min0}{\revtim\yr0\mo0\dy0\hr0\min0}{\printim\yr0\mo0\dy0\hr0\min0}{\comment OpenOffice}{\vern41130}}\deftab709

{\*\pgdsctbl
{\pgdsc0\pgdscuse195\pgwsxn11906\pghsxn16838\marglsxn1134\margrsxn1134\margtsxn1134\margbsxn1134\pgdscnxt0 Default;}}
\formshade\paperh16838\paperw11906\margl1134\margr1134\margt1134\margb1134\sectd\sbknone\sectunlocked1\pgndec\pgwsxn11906\pghsxn16838\marglsxn1134\margrsxn1134\margtsxn1134\margbsxn1134\ftnbj\ftnstart1\ftnrstcont\ftnnar\aenddoc\aftnrstcont\aftnstart1\aftnnrlc
\pgndec\pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
#!/usr/bin/env python3}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
# -*- coding: utf-8 -*-}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
import os}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
os.environ["CHROMA_DISABLE_TELEMETRY"] = "true"}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
os.environ["ANONYMIZED_TELEMETRY"] = "false"}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
from flask import Flask, request, jsonify}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
from flask_cors import CORS}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
from flask_jwt_extended import (}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
    }{\rtlch \ltrch\loch
JWTManager, create_access_token,}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
    }{\rtlch \ltrch\loch
jwt_required, get_jwt_identity}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
)}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
from werkzeug.security import generate_password_hash, check_password_hash}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
from llama_cpp import Llama}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
from langchain_text_splitters import RecursiveCharacterTextSplitter}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
from langchain_community.vectorstores import Chroma}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
from langchain_community.embeddings import HuggingFaceEmbeddings}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
from langchain_community.document_loaders import (}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
    }{\rtlch \ltrch\loch
DirectoryLoader, PyPDFLoader, TextLoader, Docx2txtLoader}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
)}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
from langchain_core.documents import Document}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
import docx2txt}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
from datetime import timedelta}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
import traceback}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
# ------------------------------------------------------------------------------}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
# Flask & auth setup}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
# ------------------------------------------------------------------------------}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
app = Flask(__name__)}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
CORS(app)}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
app.config["JWT_SECRET_KEY"] = "CHANGE_THIS_SECRET_FOR_PROD"}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=12)}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
jwt = JWTManager(app)}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
users_db = \{\}                  # \{username: \{password, email, role\}\}}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
conversation_history = \{\}      # \{username: [\{"question":..., "answer":...\}, ...]\}}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
# ------------------------------------------------------------------------------}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
# LLaMA model}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
# ------------------------------------------------------------------------------}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
llm = None}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
def initialize_llama_model(model_path="./llama-2-7b.Q4_0.gguf"):}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
    }{\rtlch \ltrch\loch
global llm}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
    }{\rtlch \ltrch\loch
if not os.path.exists(model_path):}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
print(f"\u10060\'3f Model file not found at \{model_path\}")}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
return False}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
    }{\rtlch \ltrch\loch
try:}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
print("\u55357\'3f\u56580\'3f Loading LLaMA model...")}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
llm = Llama(}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
            }{\rtlch \ltrch\loch
model_path=model_path,}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
            }{\rtlch \ltrch\loch
n_ctx=2048,}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
            }{\rtlch \ltrch\loch
n_threads=4,}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
            }{\rtlch \ltrch\loch
n_gpu_layers=0,}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
            }{\rtlch \ltrch\loch
verbose=False}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
)}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
print("\u9989\'3f LLaMA loaded")}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
return True}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
    }{\rtlch \ltrch\loch
except Exception as e:}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
print("\u10060\'3f Error loading LLaMA:", e)}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
traceback.print_exc()}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
return False}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
# ------------------------------------------------------------------------------}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
# Embeddings & Chroma vector store}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
# ------------------------------------------------------------------------------}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
embeddings = None}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
vectorstore = None}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
def initialize_embeddings():}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
    }{\rtlch \ltrch\loch
global embeddings}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
    }{\rtlch \ltrch\loch
try:}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
local_path = "./local_models/all-MiniLM-L6-v2"}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
print("\u55357\'3f\u56580\'3f Loading embeddings...")}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
if os.path.exists(local_path):}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
            }{\rtlch \ltrch\loch
print(f"Using local embeddings at \{local_path\}")}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
            }{\rtlch \ltrch\loch
model_name = local_path}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
else:}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
            }{\rtlch \ltrch\loch
print("Using HF model sentence-transformers/all-MiniLM-L6-v2")}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
            }{\rtlch \ltrch\loch
model_name = "sentence-transformers/all-MiniLM-L6-v2"}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
embeddings = HuggingFaceEmbeddings(}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
            }{\rtlch \ltrch\loch
model_name=model_name,}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
            }{\rtlch \ltrch\loch
model_kwargs=\{"device": "cpu"\}}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
)}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
print("\u9989\'3f Embeddings loaded")}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
return True}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
    }{\rtlch \ltrch\loch
except Exception as e:}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
print("\u10060\'3f Error loading embeddings:", e)}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
traceback.print_exc()}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
return False}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
def load_and_process_documents(documents_path="./sop_documents"):}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
    }{\rtlch \ltrch\loch
global vectorstore}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
    }{\rtlch \ltrch\loch
print("\\n" + "=" * 60)}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
    }{\rtlch \ltrch\loch
print(f"\u55357\'3f\u56538\'3f Loading documents from: \{documents_path\}")}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
    }{\rtlch \ltrch\loch
print("=" * 60 + "\\n")}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
    }{\rtlch \ltrch\loch
docs = []}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
    }{\rtlch \ltrch\loch
if not os.path.exists(documents_path):}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
os.makedirs(documents_path, exist_ok=True)}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
print(f"\u9888\'3f\u65039\'3f  Directory created but no docs yet: \{documents_path\}")}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
return False}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
    }{\rtlch \ltrch\loch
# PDF}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
    }{\rtlch \ltrch\loch
try:}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
pdf_loader = DirectoryLoader(}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
            }{\rtlch \ltrch\loch
documents_path,}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
            }{\rtlch \ltrch\loch
glob="**/*.pdf",}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
            }{\rtlch \ltrch\loch
loader_cls=PyPDFLoader}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
)}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
pdf_docs = pdf_loader.load()}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
docs.extend(pdf_docs)}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
print(f"\u55357\'3f\u56516\'3f Loaded \{len(pdf_docs)\} PDF docs")}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
    }{\rtlch \ltrch\loch
except Exception as e:}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
print("\u9888\'3f\u65039\'3f Error loading PDFs:", e)}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
    }{\rtlch \ltrch\loch
# TXT}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
    }{\rtlch \ltrch\loch
try:}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
txt_loader = DirectoryLoader(}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
            }{\rtlch \ltrch\loch
documents_path,}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
            }{\rtlch \ltrch\loch
glob="**/*.txt",}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
            }{\rtlch \ltrch\loch
loader_cls=TextLoader}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
)}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
txt_docs = txt_loader.load()}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
docs.extend(txt_docs)}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
print(f"\u55357\'3f\u56541\'3f Loaded \{len(txt_docs)\} TXT docs")}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
    }{\rtlch \ltrch\loch
except Exception as e:}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
print("\u9888\'3f\u65039\'3f Error loading TXTs:", e)}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
    }{\rtlch \ltrch\loch
# DOCX}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
    }{\rtlch \ltrch\loch
try:}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
docx_loader = DirectoryLoader(}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
            }{\rtlch \ltrch\loch
documents_path,}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
            }{\rtlch \ltrch\loch
glob="**/*.docx",}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
            }{\rtlch \ltrch\loch
loader_cls=Docx2txtLoader}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
)}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
docx_docs = docx_loader.load()}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
docs.extend(docx_docs)}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
print(f"\u55357\'3f\u56536\'3f Loaded \{len(docx_docs)\} DOCX docs")}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
    }{\rtlch \ltrch\loch
except Exception as e:}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
print("\u9888\'3f\u65039\'3f Error loading DOCX:", e)}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
    }{\rtlch \ltrch\loch
# Legacy .doc via docx2txt (best effort)}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
    }{\rtlch \ltrch\loch
try:}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
doc_files = []}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
for root, _, files in os.walk(documents_path):}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
            }{\rtlch \ltrch\loch
for f in files:}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
                }{\rtlch \ltrch\loch
if f.lower().endswith(".doc") and not f.lower().endswith(".docx"):}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
                    }{\rtlch \ltrch\loch
doc_files.append(os.path.join(root, f))}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
doc_count = 0}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
for path in doc_files:}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
            }{\rtlch \ltrch\loch
try:}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
                }{\rtlch \ltrch\loch
text = docx2txt.process(path)}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
                }{\rtlch \ltrch\loch
if text and text.strip():}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
                    }{\rtlch \ltrch\loch
docs.append(Document(page_content=text, metadata=\{"source": path\}))}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
                    }{\rtlch \ltrch\loch
doc_count += 1}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
            }{\rtlch \ltrch\loch
except Exception as e:}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
                }{\rtlch \ltrch\loch
print(f"\u9888\'3f\u65039\'3f Error loading \{os.path.basename(path)\}:", e)}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
print(f"\u55357\'3f\u56535\'3f Loaded \{doc_count\} DOC docs (best effort)")}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
    }{\rtlch \ltrch\loch
except Exception as e:}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
print("\u9888\'3f\u65039\'3f Error scanning DOC files:", e)}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
    }{\rtlch \ltrch\loch
if not docs:}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
print("\\n\u10060\'3f No documents loaded. Put SOP files into ./sop_documents")}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
return False}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
    }{\rtlch \ltrch\loch
print(f"\\n\u9989\'3f Total loaded: \{len(docs)\} docs")}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
    }{\rtlch \ltrch\loch
splitter = RecursiveCharacterTextSplitter(}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
chunk_size=700,}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
chunk_overlap=100,}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
length_function=len,}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
    }{\rtlch \ltrch\loch
)}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
    }{\rtlch \ltrch\loch
chunks = splitter.split_documents(docs)}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
    }{\rtlch \ltrch\loch
print(f"\u9989\'3f Created \{len(chunks)\} chunks")}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
    }{\rtlch \ltrch\loch
print("\u55357\'3f\u56580\'3f Building Chroma vector store...")}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
    }{\rtlch \ltrch\loch
vectorstore = Chroma.from_documents(}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
documents=chunks,}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
embedding=embeddings,}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
persist_directory="./chroma_db"}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
    }{\rtlch \ltrch\loch
)}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
    }{\rtlch \ltrch\loch
print("\u9989\'3f Chroma vector store ready\\n")}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
    }{\rtlch \ltrch\loch
return True}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
def query_documents(question, k=4):}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
    }{\rtlch \ltrch\loch
if vectorstore is None:}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
return None}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
    }{\rtlch \ltrch\loch
try:}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
docs = vectorstore.similarity_search(question, k=k)}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
if not docs:}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
            }{\rtlch \ltrch\loch
return None}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
context = "\\n\\n".join(d.page_content for d in docs)}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
print("\u55357\'3f\u56590\'3f Context Sent to Model:\\n", context[:800], "\\n---")}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
return context}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
    }{\rtlch \ltrch\loch
except Exception as e:}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
print("\u10060\'3f Error querying Chroma:", e)}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
traceback.print_exc()}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
return None}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
# ------------------------------------------------------------------------------}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
# LLM answer generation (RAG prompt)}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
# ------------------------------------------------------------------------------}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
def generate_answer(question, context, conversation_context=""):}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
    }{\rtlch \ltrch\loch
prompt = f"""}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
You are an AI assistant for an IT organization. You must answer questions ONLY from the SOP context.}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
SOP CONTEXT:}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
\{context\}}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
PREVIOUS CONVERSATION (optional):}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
\{conversation_context\}}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
QUESTION:}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
\{question\}}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
RESPONSE RULES:}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
- Answer ONLY using the SOP CONTEXT above.}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
- If the answer is not clearly present in the context, reply exactly:}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
  }{\rtlch \ltrch\loch
"I don't have information about this in the SOP documents."}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
- Do NOT invent or guess.}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
- Answer in clear, concise English in 1-3 sentences.}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
ANSWER:}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
"""}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
    }{\rtlch \ltrch\loch
try:}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
print(f"\u55358\'3f\u56596\'3f Calling LLaMA, q: \{question[:60]\}...")}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
resp = llm(}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
            }{\rtlch \ltrch\loch
prompt,}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
            }{\rtlch \ltrch\loch
max_tokens=256,}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
            }{\rtlch \ltrch\loch
temperature=0.1,   # low temperature to reduce hallucination}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
            }{\rtlch \ltrch\loch
top_p=0.9,}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
            }{\rtlch \ltrch\loch
repeat_penalty=1.05,}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
            }{\rtlch \ltrch\loch
stop=["QUESTION:", "SOP CONTEXT:"],}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
            }{\rtlch \ltrch\loch
echo=False,}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
)}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
raw = resp["choices"][0]["text"].strip()}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
print("\u55357\'3f\u56523\'3f Raw LLaMA answer:", repr(raw[:200]))}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
# Fallbacks}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
if not raw:}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
            }{\rtlch \ltrch\loch
return "I don't have information about this in the SOP documents."}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
# If model just repeats question, treat as failure}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
if raw.lower() == question.lower():}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
            }{\rtlch \ltrch\loch
return "I don't have information about this in the SOP documents."}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
return raw}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
    }{\rtlch \ltrch\loch
except Exception as e:}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
print("\u10060\'3f Error generating answer:", e)}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
traceback.print_exc()}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
return "I encountered an error while processing your question. Please try again."}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
# ------------------------------------------------------------------------------}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
# Auth endpoints}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
# ------------------------------------------------------------------------------}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
@app.route("/api/register", methods=["POST"])}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
def register():}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
    }{\rtlch \ltrch\loch
try:}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
data = request.get_json() or \{\}}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
username = data.get("username", "").strip()}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
password = data.get("password", "").strip()}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
email = data.get("email", "").strip()}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
if len(username) < 3 or len(password) < 6:}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
            }{\rtlch \ltrch\loch
return jsonify(\{"error": "Invalid username or password"\}), 400}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
if username in users_db:}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
            }{\rtlch \ltrch\loch
return jsonify(\{"error": "Username already exists"\}), 400}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
users_db[username] = \{}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
            }{\rtlch \ltrch\loch
"password": generate_password_hash(password),}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
            }{\rtlch \ltrch\loch
"email": email,}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
            }{\rtlch \ltrch\loch
"role": "user",}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
\}}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
conversation_history[username] = []}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
return jsonify(\{"message": "User registered", "username": username\}), 201}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
    }{\rtlch \ltrch\loch
except Exception as e:}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
print("\u10060\'3f register error:", e)}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
return jsonify(\{"error": "Registration failed"\}), 500}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
@app.route("/api/login", methods=["POST"])}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
def login():}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
    }{\rtlch \ltrch\loch
try:}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
data = request.get_json() or \{\}}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
username = data.get("username", "").strip()}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
password = data.get("password", "").strip()}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
user = users_db.get(username)}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
if not user or not check_password_hash(user["password"], password):}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
            }{\rtlch \ltrch\loch
return jsonify(\{"error": "Invalid username or password"\}), 401}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
token = create_access_token(identity=username)}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
return jsonify(\{"access_token": token, "username": username\}), 200}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
    }{\rtlch \ltrch\loch
except Exception as e:}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
print("\u10060\'3f login error:", e)}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
return jsonify(\{"error": "Login failed"\}), 500}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
@app.route("/api/profile", methods=["GET"])}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
@jwt_required()}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
def profile():}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
    }{\rtlch \ltrch\loch
current_user = get_jwt_identity()}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
    }{\rtlch \ltrch\loch
user = users_db.get(current_user)}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
    }{\rtlch \ltrch\loch
if not user:}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
return jsonify(\{"error": "User not found"\}), 404}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
    }{\rtlch \ltrch\loch
return jsonify(\{}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
"username": current_user,}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
"email": user.get("email", ""),}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
"role": user.get("role", "user"),}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
"conversation_count": len(conversation_history.get(current_user, [])),}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
    }{\rtlch \ltrch\loch
\}), 200}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
# ------------------------------------------------------------------------------}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
# Query & conversation endpoints}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
# ------------------------------------------------------------------------------}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
@app.route("/api/query", methods=["POST"])}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
@jwt_required()}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
def query():}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
    }{\rtlch \ltrch\loch
try:}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
current_user = get_jwt_identity()}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
data = request.get_json() or \{\}}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
question = (data.get("question") or "").strip()}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
print("\\n" + "=" * 60)}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
print(f"\u55357\'3f\u56549\'3f Query from: \{current_user\}: \{question\}")}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
print("=" * 60)}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
if not question:}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
            }{\rtlch \ltrch\loch
return jsonify(\{"error": "Question is required"\}), 400}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
if vectorstore is None:}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
            }{\rtlch \ltrch\loch
return jsonify(\{"error": "Documents not loaded"\}, 500)}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
if llm is None:}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
            }{\rtlch \ltrch\loch
return jsonify(\{"error": "Model not loaded"\}, 500)}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
context = query_documents(question, k=4)}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
if not context:}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
            }{\rtlch \ltrch\loch
answer = "I don't have information about this in the SOP documents."}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
else:}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
            }{\rtlch \ltrch\loch
history = conversation_history.get(current_user, [])}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
            }{\rtlch \ltrch\loch
recent = history[-2:]}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
            }{\rtlch \ltrch\loch
conv_ctx = "\\n".join(}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
                }{\rtlch \ltrch\loch
f"Q: \{h['question']\}\\nA: \{h['answer']\}" for h in recent}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
            }{\rtlch \ltrch\loch
)}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
            }{\rtlch \ltrch\loch
answer = generate_answer(question, context, conv_ctx)}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
conversation_history.setdefault(current_user, []).append(}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
            }{\rtlch \ltrch\loch
\{"question": question, "answer": answer\}}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
)}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
if len(conversation_history[current_user]) > 10:}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
            }{\rtlch \ltrch\loch
conversation_history[current_user] = conversation_history[current_user][-10:]}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
print("\u9989\'3f Final answer:", answer[:200])}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
print("=" * 60 + "\\n")}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
return jsonify(\{}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
            }{\rtlch \ltrch\loch
"question": question,}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
            }{\rtlch \ltrch\loch
"answer": answer,}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
            }{\rtlch \ltrch\loch
"user": current_user,}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
            }{\rtlch \ltrch\loch
"context_used": bool(context),}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
\}), 200}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
    }{\rtlch \ltrch\loch
except Exception as e:}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
print("\u10060\'3f /api/query error:", e)}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
traceback.print_exc()}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
return jsonify(\{"error": "Error processing query"\}), 500}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
@app.route("/api/conversation/history", methods=["GET"])}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
@jwt_required()}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
def get_history():}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
    }{\rtlch \ltrch\loch
current_user = get_jwt_identity()}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
    }{\rtlch \ltrch\loch
hist = conversation_history.get(current_user, [])}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
    }{\rtlch \ltrch\loch
return jsonify(\{"user": current_user, "history": hist\}), 200}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
@app.route("/api/conversation/clear", methods=["POST"])}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
@jwt_required()}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
def clear_history():}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
    }{\rtlch \ltrch\loch
current_user = get_jwt_identity()}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
    }{\rtlch \ltrch\loch
conversation_history[current_user] = []}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
    }{\rtlch \ltrch\loch
return jsonify(\{"message": "History cleared"\}), 200}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
# ------------------------------------------------------------------------------}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
# Docs control & health}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
# ------------------------------------------------------------------------------}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
@app.route("/api/reload-documents", methods=["POST"])}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
@jwt_required()}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
def reload_documents():}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
    }{\rtlch \ltrch\loch
ok = load_and_process_documents()}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
    }{\rtlch \ltrch\loch
if not ok:}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
return jsonify(\{"error": "Failed to load SOP documents"\}), 500}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
    }{\rtlch \ltrch\loch
return jsonify(\{"message": "Documents reloaded"\}), 200}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
@app.route("/api/documents/stats", methods=["GET"])}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
@jwt_required()}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
def doc_stats():}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
    }{\rtlch \ltrch\loch
if vectorstore is None:}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
return jsonify(\{"documents_loaded": False, "total_chunks": 0\}), 200}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
    }{\rtlch \ltrch\loch
count = vectorstore._collection.count()}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
    }{\rtlch \ltrch\loch
return jsonify(\{"documents_loaded": True, "total_chunks": count\}), 200}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
@app.route("/api/health", methods=["GET"])}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
def health():}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
    }{\rtlch \ltrch\loch
return jsonify(\{}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
"status": "ok",}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
"model_loaded": llm is not None,}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
"embeddings_loaded": embeddings is not None,}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
"documents_loaded": vectorstore is not None,}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
"total_users": len(users_db),}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
    }{\rtlch \ltrch\loch
\}), 200}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
@app.route("/", methods=["GET"])}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
def index():}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
    }{\rtlch \ltrch\loch
return jsonify(\{}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
"application": "SOP LLaMA Chatbot",}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
"version": "1.0",}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
    }{\rtlch \ltrch\loch
\}), 200}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
# ------------------------------------------------------------------------------}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
# Main}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
# ------------------------------------------------------------------------------}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
if __name__ == "__main__":}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
    }{\rtlch \ltrch\loch
print("\\n" + "=" * 60)}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
    }{\rtlch \ltrch\loch
print("\u55357\'3f\u56960\'3f Starting SOP LLaMA Chatbot")}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
    }{\rtlch \ltrch\loch
print("=" * 60 + "\\n")}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
    }{\rtlch \ltrch\loch
os.makedirs("./sop_documents", exist_ok=True)}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
    }{\rtlch \ltrch\loch
emb_ok = initialize_embeddings()}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
    }{\rtlch \ltrch\loch
llama_ok = initialize_llama_model()}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
    }{\rtlch \ltrch\loch
if emb_ok:}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
load_and_process_documents()}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
    }{\rtlch \ltrch\loch
else:}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
        }{\rtlch \ltrch\loch
print("\u9888\'3f\u65039\'3f Embeddings not loaded; skipping docs")}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch\loch
}
\par \pard\plain \s0\nowidctlpar{\*\hyphen2\hyphlead2\hyphtrail2\hyphmax0}\cf0\hich\af6\langfe2052\dbch\af4\afs24\lang1081\loch\f0\fs24\lang16393{\rtlch \ltrch
    }{\rtlch \ltrch\loch
app.run(host="0.0.0.0", port=5000, debug=True, threaded=True)}
\par }