from typing import Any, Dict, List, Mapping, Optional
from pydantic import Extra, Field, root_validator
from langchain.llms.base import LLM
from langchain.llms.utils import enforce_stop_tokens
from langchain.utils import get_from_dict_or_env
import os
import importlib
from transformers import pipeline as hf_pipeline
from  pydantic import BaseModel
DEFAULT_MODEL_ID = "llama-7b-hf"
DEFAULT_TASK = "text-generation"
VALID_TASKS = ("text2text-generation", "text-generation")
class HuggingFacePipeline(LLM, BaseModel):
    """Wrapper around HuggingFace Pipeline API.

    To use, you should have the ``transformers`` python package installed.

    Only supports `text-generation` and `text2text-generation` for now.

    Example using from_model_id:
        .. code-block:: python

            from langchain.llms import HuggingFacePipeline
            hf = HuggingFacePipeline.from_model_id(
                model_id="gpt2", task="text-generation"
            )
    Example passing pipeline in directly:
        .. code-block:: python

            from langchain.llms import HuggingFacePipeline
            from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

            model_id = "gpt2"
            tokenizer = AutoTokenizer.from_pretrained(model_id)
            model = AutoModelForCausalLM.from_pretrained(model_id)
            pipe = pipeline(
                "text-generation", model=model, tokenizer=tokenizer, max_new_tokens=10
            )
            hf = HuggingFacePipeline(pipeline=pipe)
    """

    model: Any  #: :meta private:
    tokenizer: str
    """Model name to use."""
    model_kwargs: Optional[dict] = None
    """Key word arguments to pass to the model."""

    class Config:
        """Configuration for this pydantic object."""

        extra = Extra.forbid

    # @classmethod
    # def from_model_id(
    #         cls,
    #         model_id: str,
    #         task: str,
    #         device: int = -1,
    #         model_kwargs: Optional[dict] = None,
    #         **kwargs: Any,
    # ) -> LLM:
    #     # """Construct the pipeline object from model_id and task."""
    #     # try:
    #     #     from transformers import (
    #     #         LLaMAForCausalLM,
    #     #         LLaMATokenizer,
    #     #     )
    #     #     from transformers import pipeline as hf_pipeline
    #     #
    #     # except ImportError:
    #     #     raise ValueError(
    #     #         "Could not import transformers python package. "
    #     #         "Please it install it with `pip install transformers`."
    #     #     )
    #
    #     _model_kwargs = model_kwargs or {}
    #     tokenizer = LLaMATokenizer.from_pretrained(model_id, **_model_kwargs)
    #
    #     try:
    #         if task == "text-generation":
    #             model = LLaMAForCausalLM.from_pretrained(model_id,
    #                                                      load_in_8bit=True,
    #                                                      device_map='auto')
    #         else:
    #             raise ValueError(
    #                 f"Got invalid task {task}, "
    #                 f"currently only {VALID_TASKS} are supported"
    #             )
    #     except ImportError as e:
    #         raise ValueError(
    #             f"Could not load the {task} model due to missing dependencies."
    #         ) from e
    #
    #     if importlib.util.find_spec("torch") is not None:
    #         import torch
    #
    #         cuda_device_count = torch.cuda.device_count()
    #         if device < -1 or (device >= cuda_device_count):
    #             raise ValueError(
    #                 f"Got device=={device}, "
    #                 f"device is required to be within [-1, {cuda_device_count})"
    #             )
    #         if device < 0 and cuda_device_count > 0:
    #             print(
    #                 "Device has %d GPUs available. "
    #                 "Provide device={deviceId} to `from_model_id` to use available"
    #                 "GPUs for execution. deviceId is -1 (default) for CPU and "
    #                 "can be a positive integer associated with CUDA device id.",
    #                 cuda_device_count,
    #             )
    #
    #     pipeline = hf_pipeline(
    #         task=task,
    #         model=model,
    #         tokenizer=tokenizer,
    #         device=device,
    #         model_kwargs=_model_kwargs,
    #     )
    #     if pipeline.task not in VALID_TASKS:
    #         raise ValueError(
    #             f"Got invalid task {pipeline.task}, "
    #             f"currently only {VALID_TASKS} are supported"
    #         )
    #     return cls(
    #         pipeline=pipeline,
    #         model_id=model_id,
    #         model_kwargs=_model_kwargs,
    #         **kwargs,
    #     )

    @property
    def _identifying_params(self) -> Mapping[str, Any]:
        """Get the identifying parameters."""
        return {
            **{"model_id": self.model_id},
            **{"model_kwargs": self.model_kwargs},
        }

    @property
    def _llm_type(self) -> str:
        return "huggingface_pipeline"

    def _call(self, prompt: str, stop: Optional[List[str]] = None) -> str:
        input_ids = self.tokenizer(prompt, return_tensors='pt').input_ids.cuda()
        output = self.model.generate(inputs=input_ids, temperature=0.7, do_sample=True, top_p=0.95, top_k=40,
                                max_new_tokens=512, repetition_penalty=1.1)
        text = self.tokenizer.decode(output[0])
        return text

model = 1
tokenizer = 2
HuggingFacePipeline(model=model,tokenizer=tokenizer)